import os
import uvicorn
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.router import router

app = FastAPI(
    title="Text Intelligence",
    description="FastAPI service for TEXT AI Engine",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(router)


def create_auth_file():
    auth_data = {"auth": False, "clientId": None}
    file_path = "resources/auth.json"
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            print(f"Error creating directory {directory}: {e}")
            return

    try:
        with open(file_path, "w") as f:
            json.dump(auth_data, f)
        print(f"Successfully created {file_path}")
    except OSError as e:
        print(f"Error writing to {file_path}: {e}")


if __name__ == "__main__":
    create_auth_file()
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8001,
    )
