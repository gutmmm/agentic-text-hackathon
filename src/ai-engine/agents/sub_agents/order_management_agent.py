import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.csv_toolkit import CsvTools

load_dotenv()


print(os.getcwd())
orders = "/csv/orders.csv"


order_management_agent = Agent(
    name="ORDER_MANAGEMENT_AGENT",
    model=OpenAIChat("gpt-4o"),
    tools=[CsvTools(csvs=[orders])],
    role="You are responsible to manage the order. First you need to always read the file. If a client asks for a product, you need to check the inventory and confirm the order.",
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
)
