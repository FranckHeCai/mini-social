from datetime import datetime, timezone
import re
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

class Base(DeclarativeBase):
  __abstract__ = True

  @declared_attr
  @classmethod
  def __tablename__(cls: type["Base"]) -> str:
    """Generate the table name automatically from the class name.

      This method returns the lowercased class name as the table name.

      Returns:
          str: The table name.
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
  

class BaseTimestamps(Base):
  __abstract__ = True
  
  created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    default= datetime.now(timezone.utc),
    nullable=False
  )