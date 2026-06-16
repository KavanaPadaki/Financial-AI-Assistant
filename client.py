import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():

    client = MultiServerMCPClient(
        {
            "finance": {
                "command": "python",
                "args": ["mcp_server.py"],
                "transport": "stdio"
            }
        }
    )

    tools = await client.get_tools()

    print("\nTOOLS FOUND:\n")

    for tool in tools:
        print(tool.name)

asyncio.run(main())