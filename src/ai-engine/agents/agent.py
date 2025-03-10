import os
from dotenv import load_dotenv
from swarms import Agent
from swarm_models import OpenAIChat

load_dotenv()

# Initialize the language model
llm = OpenAIChat(
    temperature=0.1, model_name="gpt-4o-mini", max_tokens=1000
)

def run_agent(message: dict):
  ## Initialize the workflow
  agent = Agent(llm=llm, max_loops=1, autosave=True, dashboard=True)
  
  # Run the workflow on a task
  response = agent.run(message['message'])
  print(response)
  return response
