from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.api.routes.addresses import router as addresses_router
from app.db.session import Base, engine
from app.models import address as address_model
from app.logging_config import configure_logging


configure_logging()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Creating database tables if they do not already exist")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables ready")
    yield

app = FastAPI(title="FastAPI Booking", lifespan=lifespan)

app.include_router(addresses_router)


@app.get("/")
def read_root() -> dict[str, str]:
    logger.debug("Root health endpoint requested")
    return {"message": "Hello, World!"}
