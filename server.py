from fastmcp import FastMCP

mcp = FastMCP("MCP with auth")


@mcp.tool()
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
