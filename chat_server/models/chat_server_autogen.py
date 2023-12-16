from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import FetchedValue
from sqlalchemy.sql import func
import uuid

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChatServerMessage(Base):
    __tablename__ = 'chat_server_messages'

    id = Column(UUID, primary_key=True, server_default=FetchedValue())
    username = Column(String(64))
    message = Column(String(500))
    updated_at = Column(DateTime(timezone=True), default=func.now())
    created_at = Column(DateTime(timezone=True), default=func.now())
