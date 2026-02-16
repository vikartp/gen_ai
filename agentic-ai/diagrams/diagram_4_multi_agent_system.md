# Agent 4: Multi-Agent System Architecture

```mermaid
graph TD
    Start([User Request]) --> Sup[Supervisor]
    Sup --> |Route Decision| Check{Task Tracking}
    
    Check -->|No Research Yet| R[Researcher Agent]
    Check -->|No Calc Yet| C[Calculator Agent]
    Check -->|No Summary Yet| S[Summarizer Agent]
    Check -->|All Done| End([Final Answer])
    
    R -->|Search Results| Sup
    C -->|Profit Calc| Sup
    S -->|Summary| Sup
    
    R -.->|DuckDuckGo| Tool1[Search Tool]
    C -.->|profit_calc| Tool2[Math Tool]
    S -.->|summarize| Tool3[Summary Tool]
    
    style Sup fill:#f96,stroke:#333,stroke-width:4px
    style R fill:#9cf,stroke:#333,stroke-width:2px
    style C fill:#9cf,stroke:#333,stroke-width:2px
    style S fill:#9cf,stroke:#333,stroke-width:2px
    style Check fill:#ff9,stroke:#333,stroke-width:2px
```

## Description

Multi-agent orchestration system showing:

**Supervisor (Red)**: Central coordinator that routes tasks
**Task Tracking (Yellow)**: Monitors what's been completed
**Specialist Agents (Blue)**:
- **Researcher**: Handles information gathering
- **Calculator**: Performs mathematical operations
- **Summarizer**: Generates summaries

**Flow**:
1. User request arrives at supervisor
2. Supervisor checks task completion status
3. Routes to appropriate specialist based on what's pending
4. Specialist completes work and returns to supervisor
5. Loop continues until all tasks complete
6. Final answer returned to user

**Tools** (dotted lines):
- Each specialist has access to specific tools
- Tools execute actual operations (search, math, summarization)
