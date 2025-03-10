from swarms import Agent

def run_categorize_agent(message: dict):
    try:
        agent = Agent(
            agent_name="Categorize-Agent",
            model_name="gpt-4o-mini", # CHANGE ME
            max_loops="auto",
            interactive=True,
            streaming_on=False,
        )

        # Define a structured prompt to get consistent output
        structured_prompt = f"""
        Analyze the following message and provide a structured response based on the content. If the message is a casual conversation, return "casual-conversation". If the message is more complex and requires orchestrator agaent to handle, return "orchestrator":
        Message: {message['message']}
        
        Return your analysis in the following JSON format:
        {{
            "message": "<message>",
            "type": <"casual-conversation" | "orchestrator">,
        }}
        """

        response = agent.run(structured_prompt)
        return response
    finally:
        print("Finally", agent)
        if 'agent' in locals():
            agent.close()  # Add this method if not available in Agent class
