from fastapi import FastAPI
from webhook import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

app.include_router(router)
