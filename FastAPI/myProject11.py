from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings

app = FastAPI()

#Alloworigin( front-end url)
origins = settings.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"], # get, put, post, delete,
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {
        "message":"CORS Enable API"
    }