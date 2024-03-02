import asyncio
import os

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")

uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
client = AsyncIOMotorClient(uri, server_api=ServerApi("1"))


async def ping_server():
    while True:
        try:
            await client.admin.command("ping")
            print("You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
            await asyncio.sleep(2)


asyncio.run(ping_server())
