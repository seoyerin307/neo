.PHONY: run clean install

MCP_PORT=6274
PROXY_PORT=6277

run:
	echo 'Starting fastmcp Server...'
	@FASTMCP_TIMEOUT=30000000 npx @modelcontextprotocol/inspector fastmcp run main.PHONY

stop:
	@echo "Cleaning up running Server..."
	@-lsof -ti:$(MCP_PORT) | xargs kill -9 2>/dev/null || true

install:
	@echo "Install dependencies..."
	@pip install openai
	@npm install -g modelcontextprotocol/inspector

restart: stop run

help:
	@echo "Available commands:"
	@echo "  make run"
	@echo "  make stop - Start the FastMCP Server"
	@echo "  make install = Install dependencies"
	@echo "  make restart - Restart the FastMCP Server"
	@echo "  make help - Show this help massage"