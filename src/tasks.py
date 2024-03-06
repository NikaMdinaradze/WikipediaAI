from src.db import collection
from src.llm import map_reduce_summarization
from src.wikipedia import retrieve_topic_data


async def retrieve_summarize_write_task(page_id: int, fresh: bool) -> None:
    """
    Background task for retrieving topic data from Wikipedia API,
    summarizing it, and writing it to the database.
    """

    existing_document = collection.find_one({"page_id": page_id})
    if existing_document:
        if fresh:
            await collection.find_one_and_delete({"page_id": page_id})
        elif not fresh:
            return None

    response = await retrieve_topic_data(page_id)

    title = response["query"]["pages"][str(page_id)]["title"]
    topic = response["query"]["pages"][str(page_id)]["extract"]
    summarized_topic = map_reduce_summarization(topic)

    await collection.insert_one(
        {"page_id": page_id, "title": title, "summarized_topic": summarized_topic}
    )
