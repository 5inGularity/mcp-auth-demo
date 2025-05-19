import asyncio
from fastmcp import Client


client = Client("http://localhost:8000/mcp")


async def main():
    async with client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")


asyncio.run(main())
