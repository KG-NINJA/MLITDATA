# main.py
import os
import requests
from fastapi import FastAPI

app = FastAPI()

API_KEY = os.environ.get("MLIT_API_KEY")
BASE_URL = "https://www.mlit-data.jp/api/v1/"

@app.get("/")
def root():
    return {"message": "MLIT Proxy Server running"}

@app.get("/search")
def search(keyword: str, limit: int = 20):
    headers = {"x-api-key": API_KEY}
    params = {"keyword": keyword, "limit": limit}

    try:
        res = requests.get(BASE_URL + "search", params=params, headers=headers)
        return res.json()
    except Exception as e:
        return {"error": str(e)}
