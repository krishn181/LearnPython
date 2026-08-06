from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home ():
    return {
        "message":"Hello from fastapi"
    }