import asyncio

from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent


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

    llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

    agent = create_agent(
        llm,
        tools
    )

    while True:

        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        response = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }
        )

        print(
            response["messages"][-1].content
        )

asyncio.run(main())