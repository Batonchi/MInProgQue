from datetime import date
from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ForeignKey, JSON
from base.database import Base
from sqlalchemy.orm import relationship


class Supporting(Base):
    __tablename__ = 'supporting'
    
    supporting_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    date_sending = Column(Date, nullable=False, default='CURRENT_TIMESTAMP')
    content = Column(JSON, nullable=False, default='{}')

    user = relationship("User", back_populates="supportings")