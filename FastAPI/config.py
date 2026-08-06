from dotenv import load_dotenv
import os

load_dotenv()

class Settings():
    ORIGINS = os.getenv("ORIGINS")
    SECRET_KEY = os.getenv("SECRET_KEY")

settings =Settings()