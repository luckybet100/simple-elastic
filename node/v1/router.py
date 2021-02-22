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
    search_results = []
    for fuzziness in range(3):
        search_results = es.search(index="museums", doc_type="museum", body={
            "query": {
                "multi_match": {
                    "query": q,
                    "fields": ["title", "city", "region"],
                    "operator": "and",
                    "analyzer": "my_search_analyzer",
                    "fuzziness": fuzziness
                },
            }
        })['hits']['hits']
        if len(search_results) != 0:
            break
    results = list(map(lambda x: x["_source"], search_results))
    return results


@router.get("/autocomplete", response_model=List[Museum])
async def autocomplete(q: str):
    es = await get_es()
    search_results = []
    for field in ["city", "title", "region"]:
        search_results = es.search(index="museums", doc_type="museum", body={
            "query": {
                "prefix": {
                    field: q,
                },
            }
        })['hits']['hits']
        if len(search_results) >= 0:
            break
    if len(search_results) == 0:
        for fuzziness in range(2, 5):
            search_results = es.search(index="museums", doc_type="museum", body={
                "query": {
                    "multi_match": {
                        "query": q,
                        "fields": ["title", "city", "region"],
                        "operator": "and",
                        "analyzer": "my_text_analyzer",
                        "fuzziness": fuzziness
                    },
                }
            })['hits']['hits']
            if len(search_results) >= 3:
                break
    results = list(map(lambda x: x["_source"], search_results))
    return results
