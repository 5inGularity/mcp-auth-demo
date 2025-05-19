from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools

from dotenv import load_dotenv
import asyncio

load_dotenv()


async def main():
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)
            print(tools)
            agent = create_react_agent("anthropic:claude-3-5-sonnet-latest", tools)
            response = await agent.ainvoke({"messages": "what's (3 + 5)"})
            print(response)


if __name__ == "__main__":
    asyncio.run(main())
