import chainlit as cl
import aiohttp


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


@cl.action_callback("action_button")
async def on_action(action: cl.Action):
    print(action.payload)


@cl.on_message
async def main(message: cl.Message):
    response = await invoke_agent(message)
    response = response.replace("\\n", "\n")
    response = response[1:-1]
    if "authorize" in response:
        actions = [
            cl.Action(
                name="action_button",
                icon="mouse-pointer-click",
                payload={"value": "authorized"},
                label="Authorize",
            )
        ]
        await cl.Message(
            content="Interact with this action button:", actions=actions
        ).send()

    await cl.Message(content=response).send()
