from typing import List

from pydantic import BaseModel


class SearchInfo(BaseModel):
    totalhits: int
    suggestion: str


class SearchResults(BaseModel):
    title: str
    snippet: str


class SearchResponse(BaseModel):
    searchinfo: SearchInfo
    results: List[SearchResults]
