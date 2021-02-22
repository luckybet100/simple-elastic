from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from node.utils.data import init_elastic
from node.v1.router import router

app = FastAPI(
    docs_url='/api/docs',
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_event_handler("startup", init_elastic)

app.include_router(router=router, prefix='/api/v1')
