from fastapi import FastAPI, Request, Response
import time
app = FastAPI()

@app.middleware("http")
async def l_middleware(request:Request, call_next):
    print("request")
    response = await call_next(request)
    print("response")
    return response

@app.middleware("http")
@app.get("/middleware")
async def log_middleware(request: Request, call_next):
    start_time = time.time()
    print("Process Start")
    response = await call_next(request)
    print(f"Process end {request.url.path}  ")
    process_end = time.time() - start_time
    print(process_end)
    return response