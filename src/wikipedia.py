import httpx


async def fetch_wikipedia_data(params: dict):
    """
    Fetch data from the Wikipedia.
    """

    url = "https://en.wikipedia.org/w/api.php"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.json()


async def search_topic(title):
    """
    Search Wikipedia topics with a given topic.
    """

    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": title,
    }
    result = await fetch_wikipedia_data(search_params)
    return result["query"]


async def retrieve_topic_data(pageids):
    """
    Retrieve topic data from Wikipedia API for specified page IDs.
    """

    title_retrieve_params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "pageids": pageids,
        "explaintext": True,
    }
    return await fetch_wikipedia_data(title_retrieve_params)
