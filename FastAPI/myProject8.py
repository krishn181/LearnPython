from fastapi import FastAPI,HTTPException, Depends,Header
from jose import jwt
from datetime import timedelta, datetime,timezone

app = FastAPI()
SECRET_KEY = "mysecret"
ALGORITHM = 'HS256'

#create token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        'exp':expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

# login api token generation
@app.post("/login")
def login(user_name:str, password:str):
    if user_name != "Admin" or password != "12345":
        raise HTTPException(status_code=401, detail="Invalid user name and password")
    token = create_token({
        'sub':user_name
    })

    return{
        "access_token":token
    }

def token_varify(token:str = Header(None)):
    try:
        payload= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,detail="Invalid or expire token")

@app.get("/secure")
def secure_data(user = Depends(token_varify)):
    return{
        "Message":"Secure data",
        "data":user
    }