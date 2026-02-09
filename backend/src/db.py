from collections.abc import AsyncGenerator

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import Depends
from src.infrastructure.orm import User, Post, Base
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
db_user= os.getenv('DB_USER')
db_password= urllib.parse.quote(os.getenv('DB_PASSWORD'))
db_host= os.getenv('DB_HOST')
db_name= os.getenv('DB_NAME')
db_port= os.getenv('DB_PORT')
DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}" 
  
engine = create_async_engine(DATABASE_URL)
async_sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_tables():
  async with engine.begin() as conn:
      # # Drop all tables
      # await conn.run_sync(Base.metadata.drop_all)
      # Create all tables
      await conn.run_sync(Base.metadata.create_all)
  print("✅ Database creation complete")

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
  async with async_sessionmaker() as session:
    yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
  yield SQLAlchemyUserDatabase(session, User)