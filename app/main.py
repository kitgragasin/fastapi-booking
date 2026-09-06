from fastapi import FastAPI

app = FastAPI(title="FastAPI Booking")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}
