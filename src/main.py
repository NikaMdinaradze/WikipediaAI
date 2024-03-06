from fastapi import BackgroundTasks, FastAPI, status

from src.schemas import SearchResponse
from src.tasks import retrieve_topic_data
from src.wikipedia import search_topic

app = FastAPI()


@app.get("/search", response_model=SearchResponse)
async def topic_search(topic: str):
    result = await search_topic(topic)
    return result


@app.post("/initiation")
async def retrieval_initiation(page_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(retrieve_topic_data, page_id)
    return {
        "status": status.HTTP_202_ACCEPTED,
        "detail": "initiation successfully accepted",
    }
