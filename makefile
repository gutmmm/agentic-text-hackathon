backend:
	cd src/ai-engine && uv run python server.py

playground:
	cd src/ai-engine && uv run python -m agents.master_agent

frontend:
	cd src/ui && uv run chainlit run main.py -w


service:
	@echo "Starting backend and frontend services..."
	@(cd src/ai-engine && uv run python server.py) & \
	(cd src/ui && uv run chainlit run main.py -w) & \
	wait

deploy:
	@echo "Starting deploy..."
	@(cd src/ai-engine && python server.py) & \
	(cd src/ui && chainlit run main.py -w) & \
	wait