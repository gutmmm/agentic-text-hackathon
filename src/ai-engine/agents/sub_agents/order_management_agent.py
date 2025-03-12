from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.csv_toolkit import CsvTools

load_dotenv()

order_management_agent = Agent(
    name="ORDER_MANAGEMENT_AGENT",
    model=OpenAIChat("gpt-4o"),
    tools=[CsvTools(csvs=["./resources/orders.csv", "./resources/products.csv"])],
    role="You are responsible to manage the order. First you need to always read the file. If a client asks for a product, you need to check the inventory and confirm the order.",
    description="",
    instructions=[],
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
    read_chat_history=True,
    read_tool_call_history=True,
    debug_mode=True,
)
