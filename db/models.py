from sqlalchemy import (
    Column, Integer, String, ForeignKey, Table
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Define models
class User(Base):
    __tablename__ = 'users'
    chat_id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

class WebLink(Base):
    __tablename__ = 'web_links'
    link_id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey('users.chat_id'))
    link = Column(String)
    tags = Column(String)
    rating = Column(Integer)