import chainlit as cl
import aiohttp

from pydantic import BaseModel
import json


class ResponseModel(BaseModel):
    agent_response: str
    need_authorization: bool


@cl.step(type="tool")
async def invoke_agent(message: cl.Message):
    print("Input message", message.content)
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
    response = await invoke_agent(message)
    response = ResponseModel(**json.loads(response))
    agent_response = response.agent_response.replace("\\n", "\n")
    if response.need_authorization:
        auth_button = cl.CustomElement(name="AuthButton")
        await cl.Message(
            content="Please authorize first:", elements=[auth_button]
        ).send()
        return

    await cl.Message(content=agent_response).send()
