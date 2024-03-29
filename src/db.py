import os

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

MONGO_USERNAME = os.getenv("DATABASE_USERNAME")
MONGO_PASSWORD = os.getenv("DATABASE_PASSWORD")
MONGO_HOST = os.getenv("DATABASE_HOST")
MONGO_PORT = os.getenv("DATABASE_PORT")

uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"

client = AsyncIOMotorClient(uri, server_api=ServerApi("1"))

database_name = "wikipedia_app"
collection_name = "analyzed_data"

database = client[database_name]
collection = database[collection_name]
