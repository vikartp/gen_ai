# file: agent_4_langgraph.py
import os
from typing import Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import END, StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
search = DuckDuckGoSearchRun()

# Shared tools
@tool
def profit_calc(revenue: float, cost: float) -> float:
    """Calculate business profit."""
    return revenue - cost

@tool
def summarize(topic: str) -> str:
    """Generate concise summary."""
    return f"Summary for {topic}: Autonomous, tool-using AI systems."

# Supervisor decides routing based on tasks completed
def supervisor(state: MessagesState) -> Literal["researcher", "calculator", "summarizer", "__end__"]:
    messages = state["messages"]
    
    # Track what's been done by checking AI messages
    ai_messages = [msg for msg in messages if isinstance(msg, AIMessage)]
    
    has_research = any("research results" in msg.content.lower() for msg in ai_messages)
    has_calc = any("calculated profit" in msg.content.lower() for msg in ai_messages)
    has_summary = any("final summary" in msg.content.lower() for msg in ai_messages)
    
    # Execute in order: research → calculate → summarize → end
    if not has_research:
        return "researcher"
    elif not has_calc:
        return "calculator"
    elif not has_summary:
        return "summarizer"
    else:
        return "__end__"

# Specialist functions
def research_agent(state: MessagesState):
    messages = state["messages"]
    query = "What is LangGraph"
    result = search.invoke(query)
    response = AIMessage(content=f"Research results for LangGraph: {result[:300]}...")
    return {"messages": [response]}

def calculator_agent(state: MessagesState):
    messages = state["messages"]
    # Extract revenue and cost from original message
    revenue = 1000000  # $1M
    cost = 700000      # $700k
    profit = profit_calc.invoke({"revenue": revenue, "cost": cost})
    response = AIMessage(content=f"Calculated profit: Revenue ${revenue:,} - Cost ${cost:,} = Profit ${profit:,}")
    return {"messages": [response]}

def summarizer_agent(state: MessagesState):
    messages = state["messages"]
    summary_text = summarize.invoke({"topic": "LangGraph and profit calculation"})
    response = AIMessage(content=f"Final {summary_text}")
    return {"messages": [response]}

# Build the graph
workflow = StateGraph(MessagesState)

# Add supervisor node (doesn't do anything, just routes)
def supervisor_node(state: MessagesState):
    return {"messages": state["messages"]}

# Add nodes
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("researcher", research_agent)
workflow.add_node("calculator", calculator_agent) 
workflow.add_node("summarizer", summarizer_agent)

# Set entry point and routing
workflow.set_entry_point("supervisor")
workflow.add_conditional_edges(
    "supervisor",
    supervisor,
    {
        "researcher": "researcher",
        "calculator": "calculator",
        "summarizer": "summarizer",
        "__end__": END
    }
)

# After each specialist, route back to supervisor
workflow.add_edge("researcher", "supervisor")
workflow.add_edge("calculator", "supervisor")
workflow.add_edge("summarizer", "supervisor")

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Multi-turn demo
config = {"configurable": {"thread_id": "multi-agent-session"}}
inputs = {"messages": [HumanMessage(content="Research LangGraph, calculate profit for $1M rev/$700k cost, then summarize.")]}

print("=== Multi-Agent Workflow Execution ===\n")
for i, chunk in enumerate(app.stream(inputs, config, stream_mode="values")):
    if "messages" in chunk and len(chunk["messages"]) > 0:
        print(f"--- Step {i+1} ---")
        print(chunk["messages"][-1].content)
        print()
