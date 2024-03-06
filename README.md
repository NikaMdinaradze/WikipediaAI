# WikipediaAI
Python application that retrieves topic-related data from Wikipedia, analyzes it with Large Language Models to generate insights, and stores the outcomes in a database.

# Development Environment Set Up

## Start project local
### Clone Project to your local environment
```bash
  git clone git@github.com:NikaMdinaradze/WikipediaAI.git
```

## Run project using docker-compose
#### Build and start containers
Build images and start containers. Migration command will be run during startup.
```bash
  make build
  make run
```

## Endpoints

### 1. Search Endpoint

- **Method:** GET
- **URL:** `/search`
- **Parameters:**
  - `topic`: The topic to search for in Wikipedia.
- **Description:** This endpoint allows users to search for a specific topic in Wikipedia. It returns title, wordcount, snippet and pageid which you should use for data retrieval initiation.

### 2. Initiation Endpoint

- **Method:** POST
- **URL:** `/initiation`
- **Parameters:**
  - `page_id`: The ID of the Wikipedia page to initiate retrieval for.
  - `fresh`: Boolean flag indicating whether to fetch fresh data or use existing data if available.
- **Description:** This endpoint is used to initiate data retrieval for a specific Wikipedia page. If the data for the given page already exists in the database and `fresh` is set to false, it returns a message indicating that the data already exists. Otherwise, it initiates a background task to retrieve, summarize, and write the data to the database.

### 3. Retrieve Endpoint

- **Method:** GET
- **URL:** `/retrieve`
- **Parameters:**
  - `page_id`: The ID of the Wikipedia page to retrieve analysis results for.
- **Description:** This endpoint is used to fetch analysis results for a specific Wikipedia page from the database. It returns the analyzed data, including the summary and other relevant information. If the data for the given page does not exist in the database, it returns a 404 Not Found error.

## Usage

To use these endpoints, send HTTP requests to the respective URLs with the required parameters. Make sure to handle the responses accordingly based on the HTTP status codes and returned data.

Example usage:

```bash
# Searching for a topic
curl -X GET "http://localhost:8000/search?topic=Python"

# Initiating data retrieval
curl -X POST "http://localhost:8000/initiation" -H "Content-Type: application/json" -d '{"page_id": 12345, "fresh": true}'

# Retrieving analysis results
curl -X GET "http://localhost:8000/retrieve?page_id=12345"
