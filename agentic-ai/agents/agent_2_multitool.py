# file: agent_2_multitool.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults  # Built-in
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

search = DuckDuckGoSearchResults()  # Real search!

@tool
def calculate_profit(revenue: float, cost: float) -> float:
    """Calculate profit from revenue and cost."""
    return revenue - cost

tools = [search, calculate_profit]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="Use search for facts, calculator for math. Reason step-by-step."
)

inputs = {
    "messages": [("user", "Search latest LangChain version. If revenue $500k and cost $350k, what's profit?")]
}

for chunk in agent.stream(inputs, stream_mode="updates"):
    if "model" in chunk:
        print(chunk["model"]["messages"][-1].content)
