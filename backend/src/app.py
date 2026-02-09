from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from src.schemas import PostSchema, PostOutSchema, UserRead, UserCreate, UserUpdate
from typing import List, Optional

from src.infrastructure.orm import User, Post
from src.db import create_db_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from contextlib import asynccontextmanager
from src.users import auth_backend, current_active_user, fastapi_users

from src.api.posts import router as post_router
from src.api.health import router as health_router

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

app.include_router(post_router)
app.include_router(health_router)


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

@app.get('/')
def root():
  return {'message' : 'WELCOME THE MINI SOCIAL MEDIA API'}

