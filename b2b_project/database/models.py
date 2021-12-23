from database import Base
from sqlalchemy import Integer,String,Column

class User_data(Base):
    __tablename__='user'
    __table_args__ = {'extend_existing': True}
    email=Column(String(255),primary_key=True,nullable=False,unique=True)
    username=Column(String(255),nullable=False,unique=True)
    password=Column(String(255),nullable=False,unique=True)

class Item(Base):
    __tablename__='items'
    __table_args__ = {'extend_existing': True}
    id=Column(Integer, primary_key=True,nullable=False,unique=True)
    item_name=Column(String(255),nullable=False,unique=True)
    item_description=Column(String(255),nullable=False,unique=True)

# def __repr__(self):
#     return f"<User_data username={self.username}"