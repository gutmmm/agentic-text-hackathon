from agno.agent import Agent
from agno.models.openai import OpenAIChat

conversation_agent = Agent(
    name="CONVERSATIONAL_AGENT",
    model=OpenAIChat("gpt-4o"),
    role="You are responsible to handle any general queries or chit-chat.",
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
)
