from sqlalchemy import TIMESTAMP, Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(TIMESTAMP, default=None, nullable=True)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="items")
