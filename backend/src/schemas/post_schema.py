from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostSchema(BaseModel):
  title: str
  content: str

class PostOutSchema(PostSchema):
  id: str
  file_path: Optional[str] = None
  file_name: Optional[str] = None
  created_at: datetime
