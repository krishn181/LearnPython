from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get('/helo')
def greeting():
    return {'message':'Welcome to main file'}

# Query Parameter
@app.get("/product")
def products(name:str=None, price : int = 0):
    return{
        "Name":name,
        "Price":price
    }

#withoutValidation
@app.post("/create-user")
def create_user(user:dict):
    return{
        "Message":"User Created",
        "data":user
            }

#Nested 
class Address(BaseModel):
    name:str
    house_num:int

class User(BaseModel):
    name:str
    address:Address

@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"user created",
        "data":user
    }