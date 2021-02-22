from asyncio import sleep

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError as ElasticConnectionError

es = None
hosts = [{'host': 'elastic', 'port': 9200}]


async def get_es():
    global es
    if not es:
        es = Elasticsearch(hosts=hosts)
    return es
