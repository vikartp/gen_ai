# Agent 2: Multi-Tool Agent Architecture

```mermaid
graph TD
    A[User: Search + Calculate] --> B[Agent Brain]
    B --> C{Which Tool?}
    C -->|Search needed| D[DuckDuckGo Search]
    C -->|Math needed| E[Calculate Profit]
    D --> F[Search Results]
    E --> G[Calculation Result]
    F --> B
    G --> B
    B --> H[Synthesized Answer]
```

## Description

Multi-tool orchestration showing:
- User asks for both search and calculation
- Agent brain intelligently selects appropriate tools
- DuckDuckGo for web search
- calculate_profit for mathematical operations
- Results flow back to agent
- Agent synthesizes final answer from multiple tool outputs
