import os

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

MONGO_USERNAME = os.getenv("DATABASE_USERNAME")
MONGO_PASSWORD = os.getenv("DATABASE_PASSWORD")
MONGO_HOST = os.getenv("DATABASE_HOST")
MONGO_PORT = os.getenv("DATABASE_PORT")

uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
client = AsyncIOMotorClient(uri, server_api=ServerApi("1"))

database = client.wikipedia_app
collection = database.get_collection("analyzed_data")
