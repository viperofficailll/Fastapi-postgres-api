from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        print("Database connected successfully")

    except SQLAlchemyError as error:
        print("Database connection failed")
        print(error)
        raise error

    yield

    engine.dispose()
    print("Database connection closed")


app = FastAPI(
    title="Game API",
    description="A simple CRUD API for managing games.",
    version="1.0.0",
    lifespan=lifespan,
)