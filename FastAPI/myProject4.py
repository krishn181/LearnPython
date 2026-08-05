from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self,name):
        self.name = name

#global exception handler 
@app.exception_handler(UserNotFoundException)
def user_not_found_exception(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code = 404,
        content={
            "status":"Error",
            "message":f"User {exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name  != "Anish":
        raise UserNotFoundException(name)
    return{
        "message":"User found"
    }