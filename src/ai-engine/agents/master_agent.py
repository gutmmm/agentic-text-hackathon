import os
import json
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app

# from agents.sub_agents.authorization_agent import authorization_agent
from agents.sub_agents.order_management_agent import order_management_agent
from agents.sub_agents.return_exchange_agent import return_exchange_agent


def verify_authorize_customer() -> str:
    # Get the absolute path to resources/auth.json
    auth_file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'auth.json')
    
    with open(auth_file_path, 'r') as f:
        auth_data = json.load(f)
        
    is_authorized = auth_data.get('auth', False)
    
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
        "First you need to check if a customer is asking some basic chit-chat questions. If so you don't need to verify him. If he is asking for checking his orders or looking through his account you need to call 'verify_authorize_customer' tool.",
        "Then proceed with other instructions. If he is not verified you should message the client with '[AUTHORIZATION_NEEDED]' message",
        "ORDER_MANAGEMENT_AGENT has the knowledge about orders, products, products categories, discounts placed in the marketplace"
        "RETURN_EXCHANGE_AGENT has the knowledge about the return and exchange policy of the marketplace."
        "If the customer inquiry is order, return or exchange specific, you can assign it to ORDER_MANAGEMENT_AGENT or RETURN_EXCHANGE_AGENT based on type of question.",
        "The response to client should not mention any usage of other agents."
        "It should stick to the point, answer the client's question. ",
    ],
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
    read_chat_history=True,
    read_tool_call_history=True,
    tools=[verify_authorize_customer],
    # show_tool_calls=True,
    debug_mode=True,
    monitoring=True,
)

### PLAYGROUND FOR TESTS PURPOSES ONLY ###
app = Playground(agents=[master_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("agents.master_agent:app", reload=True)
