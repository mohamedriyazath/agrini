import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import (
    ForeignKey,
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class pwdgen(Base):
    __tablename__ = 'pwd'
    flat_id = Column(Text, primary_key=True)
    pwd=Column(Text)
    email_id=Column(Text)
    riyas = relationship("complaint", back_populates="user")

class complaint(Base):
    __tablename__ = 'complaint_status'
    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime, server_default=func.now())
    allocate_by = Column(Text)
    title = Column(Text)
    issue = Column(Text)
    flat_id = Column(Text, ForeignKey('pwd.flat_id'))
    department=Column(Text)
    complaint_status=Column(Text)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    replay=Column(Text)
    user = relationship("pwdgen", back_populates="riyas")
