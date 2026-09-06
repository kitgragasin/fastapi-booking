from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.addresses import router as addresses_router
from app.db.session import Base, engine
from app.models import address as address_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="FastAPI Booking", lifespan=lifespan)

app.include_router(addresses_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}
