import os
import sys

from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

_agent = None


async def get_agent():
    global _agent

    if _agent is None:
        client = MultiServerMCPClient(
            {
                "finance": {
                    "command": sys.executable,
                    "args": ["mcp_server.py"],
                    "transport": "stdio",
                }
            }
        )

        tools = await client.get_tools()

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
        )

        _agent = create_agent(
            model=llm,
            tools=tools,
        )

    return _agent


async def ask(query: str):
    agent = await get_agent()

    response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query,
                }
            ]
        }
    )

    messages = response["messages"]

    return messages[-1].content
