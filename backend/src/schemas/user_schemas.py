from fastapi_users import schemas
import uuid
from datetime import datetime

class UserRead(schemas.BaseUser[uuid.UUID]):
  username: str
  created_at: datetime
  pass


class UserCreate(schemas.BaseUserCreate):
  username: str
  pass

class UserUpdate(schemas.BaseUserUpdate):
  username: str
  pass