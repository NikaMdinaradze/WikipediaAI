from src.db import collection
from src.llm import map_reduce_summarization
from src.wikipedia import retrieve_topic_data


async def retrieve_summarize_write_task(page_id: int) -> None:
    """
    Background task for retrieving topic data from Wikipedia API,
    summarizing it, and writing it to the database.
    """

    response = await retrieve_topic_data(page_id)

    title = response["query"]["pages"][str(page_id)]["title"]
    topic = response["query"]["pages"][str(page_id)]["extract"]
    summarized_topic = map_reduce_summarization(topic)

    await collection.insert_one(
        {"page_id": page_id, "title": title, "summarized_topic": summarized_topic}
    )
