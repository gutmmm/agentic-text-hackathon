from dotenv import load_dotenv
from agno.agent import RunResponse
from .boss_agent import boss_agent

load_dotenv()

def run_agent(message: dict):
  print(message)
  response: RunResponse = boss_agent.run(message['message'])

  return response.content
