import re
from typing import List

from pydantic import BaseModel, field_validator


class SearchInfo(BaseModel):
    suggestion: str
    totalhits: int


class SearchResult(BaseModel):
    title: str
    wordcount: int
    snippet: str

    @field_validator("snippet")
    def remove_html_tags(cls, value):
        pattern = re.compile("<.*?>")
        return re.sub(pattern, "", value)


class SearchResponse(BaseModel):
    searchinfo: SearchInfo
    search: List[SearchResult]


class AnalyzedData(BaseModel):
    title: str
    summery: str
