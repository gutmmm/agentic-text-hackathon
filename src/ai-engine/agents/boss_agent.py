from agno.agent import Agent, AgentKnowledge
from agno.models.openai import OpenAIChat

order_management_agent = Agent(
    name="Order management agent",
    model=OpenAIChat("gpt-4o-mini"),
    role="You are responsible to manage the order. If a client asks for a product, you need to check the inventory and confirm the order.",
    markdown=False,
)

return_exchange_agent = Agent(
    name="Return and exchange agent",
    model=OpenAIChat("gpt-4o-mini"),
    role="You are responsible to handle any return and exchange requests. If a client asks to return or exchange a product, you need to check the return policy and process the request. You can talk to order_management_agent to check if the order that client sends is valid or not.",
    markdown=False,
)

conversation_agent = Agent(
    name="Conversation agent",
    model=OpenAIChat("gpt-4o-mini"),
    role="You are responsible to handle any general queries or chit-chat.",
    markdown=False,
)

boss_agent = Agent(
    name="Boss Agent",
    model=OpenAIChat("gpt-4o-mini"),
    team=[order_management_agent, return_exchange_agent, conversation_agent],
    instructions=[
      "You are the main boss of the team. You need to assign tasks to the team members and make sure they are working efficiently.",
      "First you need to check if client asks some generic question or some more specific question. If it's generic, you can assign it to conversation agent. If it's specific, you can assign it to order_management_agent or return_exchange_agent based on type of question.",
      "Finally you need to provide a response to the client based on the response from the team members. The response to client should not mention any usage of other agents. It should stick to the point, answer the client's question. Also stip it from markdown, it needs to be plain string."
    ],
    markdown=False,
)