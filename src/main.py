from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get(topic: str):
    return {"topic": topic}
