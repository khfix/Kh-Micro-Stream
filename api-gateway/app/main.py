from typing import Union

from fastapi import FastAPI

from .routers import aspnet_service, django_service, fastapi_service

app = FastAPI()

app.include_router(django_service.router)
app.include_router(aspnet_service.router)
app.include_router(fastapi_service.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
