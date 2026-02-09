from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from src.infrastructure.orm import BaseTimestamps
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List

class User(BaseTimestamps, SQLAlchemyBaseUserTableUUID):
  # id: Mapped[str] = mapped_column(String, nullable=False, default=uuid.uuid4)
  username: Mapped[str] = mapped_column(String, nullable=False)
  posts: Mapped[List['Post']] = relationship('Post', back_populates="user", cascade="all, delete-orphan")