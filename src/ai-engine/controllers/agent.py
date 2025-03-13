import json
from dotenv import load_dotenv
from agents.master_agent import master_agent


from pydantic import BaseModel
from langchain_openai import ChatOpenAI


load_dotenv()


class ResponseSchema(BaseModel):
    need_authorization: bool


class ResponseModel(BaseModel):
    agent_response: str
    need_authorization: bool


def run_agent(message: dict):
    with open("resources/auth.json", "r") as f:
        auth_data = json.load(f)
        if auth_data["clientId"] is None:
            clientId = ""
        else:
            clientId = auth_data["clientId"]

        message = f""" [CLIENT ID] {clientId}. \n\n {message['message']}"""

    print(message)

    response = master_agent.run(message)

    prompt = f"""
    Task: Analyze folowing response - {response.content}. 
    If this response suggests that user should authenticate himself you shoud return True. 
    Otherwise return False.
    """

    llm = ChatOpenAI(model_name="gpt-4o")
    llm = llm.with_structured_output(ResponseSchema)
    model_response = llm.invoke(prompt)

    response = ResponseModel(
        agent_response=response.content,
        need_authorization=model_response.need_authorization,
    )

    return response
