from fastapi import FastAPI
from sqlmodel import SQLModel

from app.core import db

from contextlib import asynccontextmanager
from app.models import Country, Subject


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(db.engine)
    yield

app = FastAPI(
    lifespan = lifespan
)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
