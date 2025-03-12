from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app

# from agents.sub_agents.authorization_agent import authorization_agent
from agents.sub_agents.order_management_agent import order_management_agent
from agents.sub_agents.return_exchange_agent import return_exchange_agent


def authorize_customer(agent: Agent) -> str:
    """Is customer authorized"""
    agent.session_state["auth"] = True
    return "Customer is authorized"


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
        "First authorize customer calling authorize_customer tool"
        # "Important! Before using any agent you should make sure the client is authorized. You should ask him to authorize himself. Use the word - 'authorize'."
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
    tools=[authorize_customer],
    # show_tool_calls=True,
    debug_mode=True,
    monitoring=True,
)

### PLAYGROUND FOR TESTS PURPOSES ONLY ###
app = Playground(agents=[master_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("agents.master_agent:app", reload=True)
