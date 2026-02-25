# file: agent_1_basic.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

model = ChatOpenAI(
    # model="gpt-4o-mini", #Open router
    model="gpt-4o", # Model zoo
    temperature=0,
    base_url= OPENAI_API_BASE
)

@tool
def web_search(query: str) -> str:
    """Search the web for current information."""
    # Mock; replace with Tavily/DuckDuckGo in prod
    return f"Search results for '{query}': Agentic AI uses tools autonomously. LangChain enables this."

tools = [web_search]

agent = create_agent(model=model, tools=tools,
                     system_prompt="You are a helpful agent that uses tools to answer questions accurately.")

inputs = {"messages": [("user", "What is agentic AI?")]}
for chunk in agent.stream(inputs, stream_mode="updates"):
    if "model" in chunk:
        print(chunk["model"]["messages"][-1].content)
