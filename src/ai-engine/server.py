import os
import uvicorn

from fastapi import FastAPI

from routers.router import router

app = FastAPI(
    title="Text Intelligence",
    description="FastAPI service for TEXT AI Engine",
    version="1.0.0",
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
    )
