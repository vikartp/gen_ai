# file: agent_1_basic.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

@tool
def web_search(query: str) -> str:
    """Search the web for current information."""
    # Mock; replace with Tavily/DuckDuckGo in prod
    return f"Search results for '{query}': Agentic AI uses tools autonomously. LangChain enables this."

tools = [web_search]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="You are a helpful agent that uses tools to answer questions accurately."
)

response = agent.invoke({"messages": [("user", "What is agentic AI?")]})
print(response["messages"][-1].content)
