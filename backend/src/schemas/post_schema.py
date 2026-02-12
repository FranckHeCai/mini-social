from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

from .user_schemas import UserRead

class PostSchema(BaseModel):
  content: str

class PostOutSchema(PostSchema):
  id: str
  user_id: UUID
  user: UserRead
  file_path: Optional[str] = None
  file_name: Optional[str] = None
  created_at: datetime
