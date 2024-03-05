from fastapi import FastAPI

from src.schemas import SearchResponse
from src.wikipedia import search_title

app = FastAPI()


@app.get("/search", response_model=SearchResponse)
async def get(topic: str):
    result = await search_title(topic)
    return result
