from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)


# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for all ORM models
class Base(DeclarativeBase):
    pass