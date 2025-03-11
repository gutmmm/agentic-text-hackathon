import json

from agno.agent import Agent
from agno.models.openai import OpenAIChat


def check_if_client_is_authorized(user_id: str) -> bool:
    """
    Use this function to check if particualr user is authorized.

    Args:
        user_id (str): Unique user ID

    Returns:
        auth (bool): Bool value wether the user is authorized or not.
    """

    auth_json = json.loads("resources/auth.json")

    return auth_json.get(user_id, False)


def authorize_client(user_id: str) -> str:
    """
    Use this function to check if particular user is authorized.

    Args:
        user_id (str): Unique user ID

    Returns:
        auth (bool): Bool value weather the user is authorized or not.
    """
    auth_json = json.loads("resources/auth.json")
    return


authorization_agent = Agent(
    name="AUTHORIZATION_AGENT",
    model=OpenAIChat("gpt-4o"),
    role="You are responsible for checking if the customer is authorized in system.",
    instructions=[
        "First you should use check_if_client_is_authorized tool to verify if client_id is authorized",
        "If client_id is authorized",
    ],
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
    read_chat_history=True,
    read_tool_call_history=True,
)
