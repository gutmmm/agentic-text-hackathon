import json
import requests

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from controllers.agent import run_agent

router = APIRouter()


class InvokeRequest:
    message: str


class InvokeResponse:
    response: str


@router.post("/invoke")
def invoke_agent(message: dict):
    return run_agent(message)


@router.get("/authorize", response_class=HTMLResponse)
def authorize():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <input> Put the client id </input>
            <button>
        </body>
    </html>
    """
