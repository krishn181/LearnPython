from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message":"Hello admin"
    }

@app.get("/add")
def addition(a:int, b:int):
    return {
        "result":a+b
    }