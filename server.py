from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request

mcp = FastMCP("MCP with auth")


@mcp.tool()
def add(a, b):
    request = get_http_request()

    auth_header = request.headers.get("authorization", "")
    print(f"auth_header {auth_header}")

    print(f"Adding {a} and {b}")
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
