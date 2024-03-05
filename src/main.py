from fastapi import FastAPI

from src.schemas import SearchResponse
from src.wikipedia import retrieve_topic_data, search_topic

app = FastAPI()


@app.get("/search", response_model=SearchResponse)
async def topic_search(topic: str):
    result = await search_topic(topic)
    return result


@app.post("/initiation")
async def retrieval_initiation(topic: str):
    result = await retrieve_topic_data(topic)
    return result
