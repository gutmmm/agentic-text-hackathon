from pydantic import BaseModel

from fastapi import APIRouter

from agents.agent import run_agent

router = APIRouter()

class InvokeRequest(BaseModel):
    message: str

class InvokeResponse(BaseModel):
    response: str


@router.post("/invoke")
def invoke_agent(message: dict):
    return run_agent(message)

