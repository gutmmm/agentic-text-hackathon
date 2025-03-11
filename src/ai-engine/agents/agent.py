from typing import Iterator
from dotenv import load_dotenv
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    # markdown=True
)

load_dotenv()

def run_agent(message: dict):
  print(message)
  response: RunResponse = agent.run(message['message'])

  return response.content
