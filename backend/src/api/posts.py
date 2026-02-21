from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from typing import List, Optional

import os
from pathlib import Path
import tempfile
import shutil
import boto3
from botocore.exceptions import ClientError
import logging
from dotenv import load_dotenv

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.users import current_active_user
from src.infrastructure.orm import Post, User
from src.schemas import PostOutSchema, PostSchema
load_dotenv()

s3_bucket_name = os.getenv('S3_BUCKET_NAME', 'mini-social-bucket')
s3_access_key = os.getenv('AWS_ACCESS_KEY_ID')
s3_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
s3_region = os.getenv('AWS_REGION', 'eu-north-1')

router= APIRouter(
  prefix='/posts',
  tags=['posts'],
  dependencies=[Depends(current_active_user)],
  responses={
    404: {"description": "Not found"},
  }
)

@router.get('/')
async def get_all_posts(user: User = Depends(current_active_user) ,session: AsyncSession = Depends(get_async_session)) -> List[PostOutSchema]:
  post_query = (
    select(Post)
    # .where(Post.user_id != user.id)
    .order_by(Post.created_at.desc())
  )
  result = await session.scalars(post_query)

  posts = [post.to_dict() for post in result]
  return posts

@router.get('/{id}')
def get_post(id: int, session: AsyncSession = Depends(get_async_session)) -> PostSchema:
  post = session.get(Post, id)
  if not post:
    raise HTTPException(
      status_code=404,
      detail='Post not found'
    )
  return post

#GET POST FROM SPECIFIC USER

@router.get('/user/{user_id}')
async def get_user_posts(user_id: str, session: AsyncSession = Depends(get_async_session)) -> List[PostOutSchema]:
  post_query = (
    select(Post)
    .where(Post.user_id == user_id)
    .order_by(Post.created_at.desc())
  )
  result = await session.scalars(post_query)

  user_posts = [post.to_dict() for post in result]

  return user_posts

@router.post('/')
async def create_post(
  content: str = Form(...), 
  file: Optional[UploadFile] = File(None), 
  session: AsyncSession = Depends(get_async_session),
  user: User = Depends(current_active_user)
):

  file_path = None
  file_name = None

  if file:
    s3 = boto3.client(
      's3',
      aws_access_key_id=s3_access_key,
      aws_secret_access_key=s3_secret_access_key,
      region_name=s3_region
    )

    try:
      with tempfile.NamedTemporaryFile(delete=False) as tmp:
          tmp.write(await file.read())
          tmp_path = tmp.name
      
      # Upload to S3 using the temp file path
      s3.upload_file(tmp_path, s3_bucket_name, os.path.basename(file.filename))
      
      # Optionally delete the temp file
      os.remove(tmp_path)

      uploaded_file_url = f"https://{s3_bucket_name}.s3.{s3_region}.amazonaws.com/{file.filename}"
      print('FILE URL: ', uploaded_file_url)
      file_path = uploaded_file_url
    except ClientError as e:
      logging.error(e)
    # temp_file_path = None

    # try:
    #   with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext()[1]) as temp_file:
    #     temp_file_path = temp_file.name
    #     shutil.copyfileobj(file.file, temp_file)
      
    #   #UPLOAD FILE TO S3 LOGIC
      
      
    # except Exception as e:
    #   print(e)
    # finally:
    #   if temp_file_path and os.path.exists(temp_file_path):
    #     # os.remove(temp_file_path)
    #     os.unlink(temp_file_path)
    #   file.file.close()

    # file_extension = Path(file.filename).suffix
    # unique_filename = f'{uuid.uuid4()}{file_extension}'
    # file_path = ''
    # file_name = file.filename
  
  new_post = Post(
    user_id = user.id,
    user= user,
    content=content,
    file_path=file_path,
    file_name=file_name
  )

  session.add(new_post)
  await session.commit()

  return {'message' : 'post created successfully'}

@router.delete('/{id}')
async def delete_post(id: str, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
  post = await session.get(Post, id)
  if not post:
    raise HTTPException(status_code=404, detail='Post not found')
  
  if post.user_id != user.id:
    raise HTTPException(status_code=403, detail="You don't have the permission to delete this post")

  await session.delete(post)
  await session.commit()

  return {"message" : "post deleted successfully"}