from dotenv import load_dotenv
from agno.agent import RunResponse
from agents.master_agent import master_agent


from pydantic import BaseModel
from langchain_community.llms import ChatOpenAI


load_dotenv()


class ResponseModel(BaseModel):
    nedd_authorization: bool


def run_agent(message: dict):
    response = master_agent.run(message["message"])

    prompt = f"""
    Task: Analyze folowing response - {response.content}. 
    If this response suggests that user should authenticate himself you shoud return True. 
    Otherwise return False.
    """

    llm = OpenAI(model_name="gpt-4o")
    llm = llm.with_structured_output(ResponseModel)
    should_authorize_response = llm.invoke(prompt)

    print(should_authorize_response)

    return {
        "agent_response": response.content,
        "should_authorize": should_authorize_response,
    }
