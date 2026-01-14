from fastapi import FastAPI
from webhook import router

app = FastAPI()


app.include_router(router)

@app.get("/")
def home():
    return {"message": "Property Management System is live"}
