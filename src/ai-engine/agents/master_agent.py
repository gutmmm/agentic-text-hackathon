from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app

# from agents.sub_agents.authorization_agent import authorization_agent
from agents.sub_agents.order_management_agent import order_management_agent
from agents.sub_agents.return_exchange_agent import return_exchange_agent

master_agent = Agent(
    name="ORCHESTRATOR",
    model=OpenAIChat("gpt-4o"),
    team=[order_management_agent, return_exchange_agent],
    description="""
        You are the orchestrating agent of the customer service team in PUMBA company marketplace.
        Your objective is to delegate the tasks to the agents at your disposal and make sure they are working efficiently.
        The ultimate goal is to solve customer inquires, questions and issues.
        You have three agents to delegate tasks to - CONVERSATIONAL_AGENT, ORDER_MANAGEMENT_AGENT and RETURN_EXCHANGE_AGENT
        """,
    instructions=[
        "CONVERSATIONAL_AGENT handles casual conversations with the customer. It does not have any specific knowledge, just answers generic inquires."
        "ORDER_MANAGEMENT_AGENT has the knowledge about orders placed in the marketplace"
        "RETURN_EXCHANGE_AGENT has the knowledge about the return and exchange policy of the marketplace."
        "If the customer inquiry is order, return or exchange specific, you can assign it to ORDER_MANAGEMENT_AGENT or RETURN_EXCHANGE_AGENT based on type of question.",
        # "Finally you need to provide a response to the client based on the response from the team members. "
        "The response to client should not mention any usage of other agents."
        # "Also if its the first message it should contain some welcome message to the client with minimum of 3 words eg. 'Welcome to our Pumba store'."
        "It should stick to the point, answer the client's question. ",
        # "Also strip it from markdown, it needs to be plain string.",
    ],
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
    read_chat_history=True,
    read_tool_call_history=True,
    # show_tool_calls=True,
)

### PLAYGROUND FOR TESTS PURPOSES ONLY ###
app = Playground(agents=[master_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("agents.master_agent:app", reload=True)
