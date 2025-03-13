import chainlit as cl
import aiohttp
import requests

from pydantic import BaseModel
import json


class ResponseModel(BaseModel):
    agent_response: str
    need_authorization: bool


@cl.on_chat_start
def on_chat_start():
    requests.get("http://0.0.0.0:8001/auth")


@cl.step()
async def Agent(message: cl.Message):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://0.0.0.0:8001/invoke", json={"message": message.content}
        ) as response:
            if response.status == 200:
                return await response.text()
            else:
                return f"Error: Received status code {response.status}"


@cl.on_message
async def main(message: cl.Message):
    response = await Agent(message)
    data = json.loads(response)
    response = ResponseModel(**data)
    agent_response = response.agent_response.replace("\\n", "\n")
    if response.need_authorization:
        auth_button = cl.CustomElement(name="AuthButton")
        await cl.Message(content=agent_response, elements=[auth_button]).send()
        return

    await cl.Message(content=agent_response).send()
