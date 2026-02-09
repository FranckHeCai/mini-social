import uuid
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from src.infrastructure.orm import BaseTimestamps

from typing import Optional

class Post(BaseTimestamps):

  id: Mapped[UUID] = mapped_column(
    UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
  )
  # id: Mapped[str] = mapped_column(
  #   String, primary_key=True, default=lambda: str(uuid.uuid4())
  # )
  user_id: Mapped[str] = mapped_column(ForeignKey('user.id', name='fk_post_user_id'), nullable=False)
  user: Mapped['User'] = relationship('User', back_populates='posts')
  title: Mapped[str] = mapped_column(String, nullable=False, index=True)
  content: Mapped[str] = mapped_column(Text, nullable=False)
  file_path: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)
  file_name: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)

  def to_dict(self):
    return {
      "id": str(self.id),
      "user_id": self.user_id,
      "title": self.title,
      "content": self.content,
      "created_at": self.created_at,
      "file_path": self.file_path,
      "file_name": self.file_name
    }