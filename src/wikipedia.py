import httpx


async def fetch_wikipedia_data(params):
    url = "https://en.wikipedia.org/w/api.php"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.json()


async def search_title(title):
    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": title,
    }
    result = await fetch_wikipedia_data(search_params)
    return result["query"]


async def retrieve_title_data(title):
    title_retrieve_params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
        "explaintext": True,
    }
    return await fetch_wikipedia_data(title_retrieve_params)
