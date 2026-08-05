from fastapi import FastAPI, HTTPException, Depends, Header

app = FastAPI()

def verify(token:str = Header(None)):
    if token != "Helo":
        raise HTTPException(
            status_code=401,
            detail="Unauthorize user"
        )
    return{
        "Message":"authorize user"
    }

@app.get("/user")
def verify_token(user = Depends(verify)):
    return {
        "message":"secure user accessed",
        "data":user
    }