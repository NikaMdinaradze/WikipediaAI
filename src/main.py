import os

from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")

# MongoDB connection
client = MongoClient(
    f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
)


@app.post("/")
def get():
    return {"message": "Hello"}
