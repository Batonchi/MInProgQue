import json

from datetime import date
from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, JSON
from base.database import Base
from sqlalchemy.orm import relationship


class Image(Base):
    __tablename__ = 'images'

    image_id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text)


class TextContent(Base):
    __tablename__ = 'texts'

    text_id = Column(Integer, primary_key=True, autoincrement=True)
    type_content = Column(Text, nullable=False, default='text')
    content = Column(Text, nullable=False, default='')


class Page(Base):
    __tablename__ = 'pages'
    
    page_id = Column(Integer, primary_key=True)
    title = Column(Text)
    author_id = Column(Integer, ForeignKey('users.user_id'))
    description = Column(Text, nullable=False, default='')
    url = Column(Text, nullable=False, default='')
    published_at = Column(Date, nullable=False, default='CURRENT_TIMESTAMP')
    content = Column(JSON, nullable=False, default='{}')

    author = relationship("User", back_populates="pages")
    feedbacks = relationship("Feedback", back_populates="page")
    favorites_rel = relationship("Favorite", back_populates="page")


class Feedback(Base):
    __tablename__ = 'feedback'
    
    feedback_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    page_id = Column(Integer, ForeignKey('pages.page_id'))
    content = Column(JSON)

    user = relationship("User", back_populates="feedbacks")
    page = relationship("Page", back_populates="feedbacks")
