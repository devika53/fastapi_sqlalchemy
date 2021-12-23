from fastapi import FastAPI,status,Depends
from database import SessionLocal
import uuid
import models

import schemas
from typing import List
from pydantic import BaseModel
from jwt_handler import signJWT
from jwt_bearer import JWTBearer


app=FastAPI()

db=SessionLocal()

#create a user
@app.post('/signup', response_model=schemas.User)
def create_user(userone:schemas.User):
    new_user=models.User_data(
        email=userone.email,
        username=userone.username,
        password=userone.password
    )
    db.add(new_user)
    db.commit()
    return  new_user

@app.post('/login')
def login(user:schemas.UserLogin):
    user_login=db.query(models.User_data).filter(models.User_data.username == user.username).first()
    if user_login is not None:
        return signJWT(user.username)

@app.post('/item', dependencies=[Depends(JWTBearer())], response_model=schemas.Item)
def create_item(item:schemas.Item):
    new_item=models.Item(
        id=item.id,
        item_name=item.item_name,
        item_description=item.item_description
    )
    db.add(new_item)
    db.commit()
    return  new_item

#get all users
@app.get('/users')
def get_users():
    items=db.query(models.User_data).all()
    return items


