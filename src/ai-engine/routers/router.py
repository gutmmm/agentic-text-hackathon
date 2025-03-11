from fastapi import APIRouter
from controllers.agent import run_agent

router = APIRouter()


class InvokeRequest:
    message: str


class InvokeResponse:
    response: str


@router.post("/invoke")
def invoke_agent(message: dict):
    return run_agent(message)
