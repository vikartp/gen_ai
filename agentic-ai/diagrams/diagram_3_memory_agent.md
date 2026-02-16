# Agent 3: Memory Agent Architecture

```mermaid
graph TD
    A[Turn 1: User Query] --> B[Agent + Tools]
    B --> C[MemorySaver]
    C -->|Store State| D[Thread: abc123]
    D --> E[Turn 2: Follow-up Query]
    E --> F[Agent Recalls Context]
    F --> C
    C -->|Load State| F
    F --> G[Contextual Response]
    
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
```

## Description

Stateful conversation with memory showing:
- **Turn 1**: Initial query processed and state saved
- **MemorySaver**: Checkpoint system storing conversation
- **Thread ID**: Session identifier (abc123)
- **Turn 2**: Follow-up query loads previous context
- **Agent Recalls**: Retrieves state from memory
- **Contextual Response**: Answer informed by conversation history

Key feature: Agent remembers previous interactions across turns.
