import chainlit as cl
import aiohttp

@cl.step(type="tool")
# async def tool(message: cl.Message):
#   # Fake tool
#   await cl.sleep(2)
#   return "Response from the tool!"

async def tool(message: cl.Message):
    print('!!! message', message.content)
    # Make HTTP request to external endpoint
    async with aiohttp.ClientSession() as session:
        async with session.post('http://0.0.0.0:8001/invoke', json={'message': message.content}) as response:
            if response.status == 200:
                return await response.text()
            else:
                return f"Error: Received status code {response.status}"
    
@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
  tool_res = await tool(message)

  await cl.Message(content=tool_res).send()