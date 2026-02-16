# Agent 1: Basic Agent Architecture

```mermaid
graph LR
    A[User Query] --> B[Agent]
    B --> C{Needs Tool?}
    C -->|Yes| D[web_search tool]
    D --> B
    C -->|No| E[Final Answer]
    E --> F[User]
```

## Description

Simple ReAct pattern showing:
- User provides a query
- Agent decides if it needs to use a tool
- If yes, calls `web_search()` and processes results
- If no, provides final answer directly
- Returns answer to user
