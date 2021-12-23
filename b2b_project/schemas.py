from pydantic import BaseModel

class User(BaseModel ):
    email:str
    username:str
    password:str

    class Config:
        orm_mode=True



class UserLogin(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode=True

class Item(BaseModel):
    id: int
    item_name: str
    item_description: str
      
    class Config:
        orm_mode=True