import json


from datetime import date
from sqlalchemy import Column, Integer, String, Boolean, Date, Text, JSON, ForeignKey, func
from base.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    is_admin = Column(Boolean, nullable=True, default=False)
    is_active = Column(Boolean, nullable=True, default=False)
    date_reg = Column(Date, nullable=False, default=func.now())
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    special_word = Column(String(40), nullable=False, default='')
    avatar = Column(Text)
    favorites = Column(JSON, nullable=False, default='{}')

    pages = relationship("Page", back_populates="author")
    feedbacks = relationship("Feedback", back_populates="user")
    supportings = relationship("Supporting", back_populates="user")
    favorites_rel = relationship("Favorite", back_populates="user")


class Favorite(Base):
    __tablename__ = 'favorite'
    
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    page_id = Column(Integer, ForeignKey('pages.page_id'), primary_key=True)
    content = Column(JSON, nullable=False, default='{}')

    user = relationship("User", back_populates="favorites_rel")
    page = relationship("Page", back_populates="favorites_rel")