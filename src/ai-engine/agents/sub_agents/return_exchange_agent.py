import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.pdf import PDFKnowledgeBase

load_dotenv()

qdrant_api_key = os.getenv("QDRANT_API_KEY")
qdrant_url = os.getenv("QDRANT_URL")

vector_db = Qdrant(collection="return-policy", url=qdrant_url, api_key=qdrant_api_key)

return_policy = PDFKnowledgeBase(
    path="../resources/Pumba_Return_Policy.pdf",
    vector_db=vector_db,
)
return_policy.load(recreate=False)

return_exchange_agent = Agent(
    name="RETURN_EXCHANGE_AGENT",
    model=OpenAIChat("gpt-4o"),
    knowledge=return_policy,
    role="You are responsible to handle any return and exchange requests. If a client asks to return or exchange a product, you need to check the return policy and process the request. You can talk to ORDER_MANAGEMENT_AGENT to check if the order that client sends is valid or not.",
    markdown=False,
    add_history_to_messages=True,
    num_history_responses=5,
    read_chat_history=True,
    read_tool_call_history=True,
    debug_mode=True,
)
