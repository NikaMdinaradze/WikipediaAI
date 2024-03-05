from fastapi import FastAPI

from src.wikipedia import search_title

app = FastAPI()


@app.get("/search")
async def get(topic: str):
    result = await search_title(topic)
    return {"topic": result}
