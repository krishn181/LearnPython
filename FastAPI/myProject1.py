from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    name : str
    age  : int

users = {}

@app.post("/user")
def create_user(user:User):
    user_id = len(users)+1
    users[user_id] = user
    return{
        "message":"user created",
        "data" : user
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id in users:
        return users[user_id]
    return {
        "error":"user not define"
    }

@app.put("/update-user/{user_id}")
def update_user(user_id:int, user:User):
    if user_id in users:
        users[user_id] = user.model_dump()
        return {
            "Message":"User update successfully"
        }
    return {
        "error":"user not found"
    }

@app.delete("/delete-user/{user_id}")
def delete_user(user_id:int):
    if user_id in users:
        users.pop(user_id)
        return {
                "Message":"User delete successfully"
                }
    return {
       "error":"user not found"
        }