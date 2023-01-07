import requests
from fastapi import FastAPI, Request
import os

user_service = os.environ.get("user_service","http://localhost:8001")
app = FastAPI()

@app.get("/get-user/{user_id}")
def get_user(user_id: str, request:Request):
    res = requests.get(f"{user_service}/user/{user_id}")
    res = res.json()
    return res