from fastapi_users import schemas
import uuid

class UserRead(schemas.BaseUser[uuid.UUID]):
  username: str
  pass


class UserCreate(schemas.BaseUserCreate):
  username: str
  pass

class UserUpdate(schemas.BaseUserUpdate):
  username: str
  pass