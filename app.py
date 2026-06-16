from fastapi import FastAPI

from agent import ask_agent

app = FastAPI(
    title="Financial AI Assistant"
)


@app.get("/")
def home():
    return {
        "message": "Financial AI Assistant is running"
    }


@app.get("/ask")
async def ask(query: str):

    response = await ask_agent(query)

    return {
        "query": query,
        "response": response
    }