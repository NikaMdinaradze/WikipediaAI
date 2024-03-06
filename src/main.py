from fastapi import BackgroundTasks, FastAPI, HTTPException, status

from src.db import collection
from src.schemas import AnalyzedData, SearchResponse
from src.tasks import retrieve_summarize_write_task
from src.wikipedia import search_topic

app = FastAPI()


@app.get("/search", response_model=SearchResponse)
async def topic_search(topic: str):
    """
    Endpoint for topic specification.
    """

    result = await search_topic(topic)
    return result


@app.post("/initiation", status_code=status.HTTP_202_ACCEPTED)
async def retrieval_initiation(
    page_id: int, fresh: bool, background_tasks: BackgroundTasks
):
    """
    Endpoint for data retrieval initiation.
    """

    document = await collection.find_one({"page_id": page_id})
    if document:
        if fresh:
            await collection.delete_one({"page_id": page_id})
        else:
            return {"detail": f"{page_id} already exists"}

    background_tasks.add_task(retrieve_summarize_write_task, page_id)
    return {"detail": "Initiation successfully accepted"}


@app.get("/retrieve", response_model=AnalyzedData)
async def retrieve_summarized_topic(page_id: int):
    """
    Endpoint for fetching analysis results from the database.
    """

    document = await collection.find_one({"page_id": page_id})
    if document:
        document["_id"] = str(document["_id"])
        return document
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found topic with {page_id}",
        )
