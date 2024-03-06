from fastapi import BackgroundTasks, FastAPI, status

from src.db import collection
from src.schemas import SearchResponse
from src.tasks import retrieve_summarize_write_task
from src.wikipedia import search_topic

app = FastAPI()


@app.get("/search", response_model=SearchResponse)
async def topic_search(topic: str):
    result = await search_topic(topic)
    return result


@app.post("/initiation")
async def retrieval_initiation(page_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(retrieve_summarize_write_task, page_id)
    return {
        "status": status.HTTP_202_ACCEPTED,
        "detail": "initiation successfully accepted",
    }


@app.get("/retrieve")
async def retrieve_summarized_topic(page_id: int):
    document = await collection.find_one({"page_id": page_id})
    if document:
        document["_id"] = str(document["_id"])
        return document
    else:
        return None
