import json

from agno.agent import Agent
from agno.models.openai import OpenAIChat


'''def check_if_client_is_authorized(user_id: str) -> bool:
    """
    Use this function to check if particualr user is authorized.

    Args:
        user_id (str): Unique user ID

    Returns:
        auth (bool): Bool value wether the user is authorized or not.
    """

    auth_json = json.loads("resources/auth.json")

    return auth_json.get(user_id, False)'''


def check_if_client_is_authorized(user_id: str) -> bool:
    """
    Use this function to check if particualr user is authorized.

    Args:
        user_id (str): Unique user ID

    Returns:
        auth (bool): Bool value wether the user is authorized or not.
    """

    # auth_json = json.loads("resources/auth.json")

    if user_id == "1234":
        return True
    else:
        return False


authorization_agent = Agent(
    name="AUTHORIZATION_AGENT",
    model=OpenAIChat("gpt-4o"),
    tools=[check_if_client_is_authorized],
    role="You are responsible for checking if the customer is authorized in system.",
    instructions=[
        "Call check_if_client_is_authorized to check if the client is autorized. True means authorized, False means not authorized."
    ],
    markdown=False,
)
