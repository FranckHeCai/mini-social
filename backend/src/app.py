from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from src.schemas import PostSchema, PostOutSchema, UserRead, UserCreate, UserUpdate
from typing import List, Optional

from src.infrastructure.orm import User, Post
from src.db import create_db_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from contextlib import asynccontextmanager
import os
import shutil
from pathlib import Path
import tempfile
from src.users import auth_backend, current_active_user, fastapi_users

@asynccontextmanager
async def lifespan(app: FastAPI):
  await create_db_tables()
  yield

app = FastAPI(lifespan=lifespan)

app.include_router(fastapi_users.get_auth_router(auth_backend), prefix='/auth/jwt', tags=['auth'])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_reset_password_router(), prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_verify_router(UserRead), prefix='/auth', tags=['auth'])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix='/users', tags=['users'])

origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods=['*'],
  allow_headers=['*']
)

@app.get('/health')
def health():
  return {'message' : 'Api working correctly!'}

@app.get('/')
def root():
  return {'message' : 'WELCOME THE MINI SOCIAL MEDIA API'}

@app.get('/feed')
async def get_all_posts(session: AsyncSession = Depends(get_async_session)) -> List[PostOutSchema]:
  post_query = select(Post).order_by(Post.created_at.desc())
  result = await session.scalars(post_query)

  posts = [post.to_dict() for post in result]
  return posts

@app.get('/posts/{id}')
def get_post(id: int) -> PostSchema:
  pass

@app.post('/posts')
async def create_post(
  title: str = Form(...), 
  content: str = Form(...), 
  file: Optional[UploadFile] = File(None), 
  session: AsyncSession = Depends(get_async_session),
  user: User = Depends(current_active_user)
):

  file_path = None
  file_name = None

  if file:

    temp_file_path = None

    try:
      with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext()[1]) as temp_file:
        temp_file_path = temp_file.name
        shutil.copyfileobj(file.file, temp_file)
      
      #UPLOAD FILE TO S3 LOGIC
      
    except Exception as e:
      print(e)
    finally:
      if temp_file_path and os.path.exists(temp_file_path):
        # os.remove(temp_file_path)
        os.unlink(temp_file_path)
      file.file.close()

    # file_extension = Path(file.filename).suffix
    # unique_filename = f'{uuid.uuid4()}{file_extension}'
    # file_path = ''
    # file_name = file.filename
  
  new_post = Post(
    user_id = user.id,
    title= title,
    content=content,
    file_path=file_path,
    file_name=file_name
  )

  session.add(new_post)
  await session.commit()

  return {'message' : 'post created successfully'}

@app.delete('/posts/{id}')
async def delete_post(id: str, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
  post = await session.get(Post, id)
  if not post:
    raise HTTPException(status_code=404, detail='Post not found')
  
  if post.user_id != user.id:
    raise HTTPException(status_code=403, detail="You don't have the permission to delete this post")

  session.delete(post)
  await session.commit()

  return {"message" : "post deleted successfully"}