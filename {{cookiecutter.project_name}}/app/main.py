import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.ds_api import ds_api
from app.settings import Settings

# log config

# general settings
settings = Settings()

app = FastAPI(
    dependencies=[],
    title="{{cookiecutter.project_name}}",
    description="""
    Template Project showcasing the creation of an FastAPI Endpoint using ML models.
    """,
    version=settings.api_version,
    terms_of_service="#",
    contact={
        "company": "the peak lab. GmbH & Co. KG",
        "url": "https://thepeaklab.com",
        "email": "{{cookiecutter.email}}",
    },
)

origins = [
    "http://localhost:4200",
]
if settings.origin:
    origins.append(settings.origin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.include_router(ds_api.router)


@app.on_event("startup")
async def startup_event():
    """This function will be called after the API is initialized"""
    logging.info("Starting API")


@app.on_event("shutdown")
async def shutdown_event():
    """This function will be called after the shutdown of the API"""
    # do something here
    logging.info("Stopping API")
