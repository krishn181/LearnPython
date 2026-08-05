from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/user_created", status_code=status.HTTP_201_CREATED)
def user_created():
    return{
        "message":"User created"
    }

@app.get("/user")
def user_get():
    return {
        "message":"user found",
        "data":{
            "name":"Anish",
            "age":24
        }
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail="User not found"
        )
    return {
        "Message":"User found"
    }