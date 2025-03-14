import os
import json
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app

from agents.sub_agents.order_management_agent import order_management_agent
from agents.sub_agents.return_exchange_agent import return_exchange_agent


def verify_authorize_customer() -> str:
    auth_file_path = os.path.join(
        os.path.dirname(__file__), "..", "resources", "auth.json"
    )

    with open(auth_file_path, "r") as f:
        auth_data = json.load(f)

    is_authorized = auth_data.get("auth", False)

    if not is_authorized:
        return "[AUTHORIZATION_NEEDED]"

    return "User authorized"


master_agent = Agent(
    name="ORCHESTRATOR",
    model=OpenAIChat("gpt-4o"),
    team=[order_management_agent, return_exchange_agent],
    description="""
        You are the orchestrating agent of the customer service team in PUMBA company marketplace.
        Your objective is to delegate the tasks to the agents at your disposal and make sure they are working efficiently.
        The ultimate goal is to solve customer inquires, questions and issues.
        You have three agents to delegate tasks to - ORDER_MANAGEMENT_AGENT and RETURN_EXCHANGE_AGENT
        """,
    instructions=[
        "Important! Before sharing any informations about orders, or proceeding with return procedure you should always check if user has authorized himself using 'verify_authorize_customer' tool.",
        "If customer is not authorized, ask him to authorize himself.",
        "You do not need to authorize agent when he is asking for casual stuff.",
        "After succesfull authorization, continue proceeding with previous customer request",
        "You should not leak any company information without authorization",
        "ORDER_MANAGEMENT_AGENT has the knowledge about orders, products, products categories, discounts placed in the marketplace, however he MUST NOT share any information about orders of other customer - there is a columnd called 'client_id', which he should take into account"
        "RETURN_EXCHANGE_AGENT has the knowledge about the return and exchange policy of the marketplace.",
        "If the customer inquiry is order, return or exchange specific, you can assign it to ORDER_MANAGEMENT_AGENT or RETURN_EXCHANGE_AGENT based on type of question.",
        "The response to client should not mention any usage of other agents.",
        "It should stick to the point, answer the client's question. ",
    ],
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
    read_chat_history=True,
    read_tool_call_history=True,
    tools=[verify_authorize_customer],
    retries=3,
)


if __name__ == "__main__":
    app = Playground(agents=[master_agent]).get_app()
    serve_playground_app("agents.master_agent:app", reload=True)
