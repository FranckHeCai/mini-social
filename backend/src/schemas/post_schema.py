from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class PostSchema(BaseModel):
  title: str
  content: str

class PostOutSchema(PostSchema):
  id: str
  user_id: UUID
  file_path: Optional[str] = None
  file_name: Optional[str] = None
  created_at: datetime
