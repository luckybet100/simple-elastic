from typing import List

from fastapi import APIRouter
from pydantic.main import BaseModel

from node import get_es

router = APIRouter()


class Museum(BaseModel):
    title: str
    city: str
    region: str


@router.get("/search", response_model=List[Museum])
async def search(q: str):
    es = await get_es()
    search_results = es.search(index="museums", doc_type="museum", body={
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["title", "city", "region"],
                "operator": "and",
                "analyzer": "my_search_analyzer",
                "fuzziness": "3"
            },
        }
    })['hits']['hits']
    results = list(map(lambda x: x["_source"], search_results))
    return results
