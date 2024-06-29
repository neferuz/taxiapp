from fastapi import FastAPI
from taxi_service.app import auth
from .dependencies import get_db

app = FastAPI()

app.include_router(auth.router)
