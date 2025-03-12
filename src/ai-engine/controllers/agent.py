from dotenv import load_dotenv
from agno.agent import RunResponse
from agents.master_agent import master_agent

load_dotenv()


def run_agent(message: dict):
    print(message)

    response: RunResponse = master_agent.run(message["message"])

    print(dir(master_agent))

    return response.content
