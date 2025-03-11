backend:
	cd src/ai-engine && uv run python server.py

playground:
	cd src/ai-engine && uv run python -m agents.master_agent

frontend:
	cd src/ui && uv run chainlit run main.py