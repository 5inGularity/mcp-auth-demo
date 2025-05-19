# MCP auth demo

A simple demo that shows how to implement authentication between MCP server and client using `authorization` header.

# Setup

```
uv venv
source .venv/bin/activate
uv pip install
```

- Place `ANTHROPIC_API_KEY` in `.env` file.

# Run the server
- `uv run server.py`

# Run the client
- `uv run agent.py`

- Logs on server will show headers sent by the client. Server can enforce authorization using the header.

```
auth_header Bearer supersecret
Adding 3 and 5
```