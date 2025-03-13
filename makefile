backend:
	cd src/ai-engine && python server.py

frontend:
	cd src/ui && chainlit run --host 0.0.0.0 --port 8000 main.py

playground:
	cd src/ai-engine && uv run python -m agents.master_agent

service:
	@echo "Starting backend and frontend services..."
	@(cd src/ai-engine && uv run python server.py) & \
	(cd src/ui && uv run chainlit run main.py -w) & \
	wait

deploy:
	@echo "Starting deploy..."
	@(cd src/ai-engine && python server.py) & \
	(cd src/ui && chainlit run --host 0.0.0.0 --port 8000 main.py) & \
	wait