from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os, shutil

app = FastAPI()

#step1 insure folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists ( UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#step2 static file setup
app.mount("/files",StaticFiles(directory=UPLOAD_DIR), name="files")


#step 3 upload file 
@app.post("/upload")
def upload_file(file:UploadFile = File(...)):
    filename = file.filename
    filepath = os.path.join(UPLOAD_DIR,filename)

    if not filename:
        raise HTTPException(status_code=400, detail="file not selected")

    with open(filepath,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return {
            "message": "File upload successfully",
            "filename":filename,
            "file_url":f"http://127.0.0.1:8000/files/{filename}"
        } 

#step 4 : get file 
@app.get("/getfile/{filename}")
def get_file(filename:str):
    filepath = os.path.join(UPLOAD_DIR,filename)
    if not os.path.exists(filepath):
        raise HTTPException(
            status_code=404,
            detail="file not found"
        )
    return {
        "file:url":f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return{
        "message":"File uploaded api running"
    }
