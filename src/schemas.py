import re
from typing import List, Optional

from pydantic import BaseModel, field_validator


class SearchInfo(BaseModel):
    suggestion: Optional[str] = None
    totalhits: int


class SearchResult(BaseModel):
    title: str
    wordcount: int
    snippet: str
    pageid: int

    @field_validator("snippet")
    def remove_html_tags(cls, value):
        pattern = re.compile("<.*?>")
        return re.sub(pattern, "", value)


class SearchResponse(BaseModel):
    searchinfo: SearchInfo
    search: List[SearchResult]


class AnalyzedData(BaseModel):
    _id: str
    page_id: int
    title: str
    summarized_topic: str
