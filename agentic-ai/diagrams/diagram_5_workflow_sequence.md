# Agent 4: Workflow Execution Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant Sup as Supervisor
    participant R as Researcher
    participant C as Calculator
    participant S as Summarizer
    
    U->>Sup: Research + Calculate + Summarize
    
    loop Task Execution
        Sup->>Sup: Check completed tasks
        
        alt No research done
            Sup->>R: Route to Researcher
            R->>R: Search "What is LangGraph"
            R-->>Sup: Research results
        
        else No calculation done
            Sup->>C: Route to Calculator
            C->>C: Calculate $1M - $700K
            C-->>Sup: Profit = $300K
        
        else No summary done
            Sup->>S: Route to Summarizer
            S->>S: Summarize findings
            S-->>Sup: Final summary
        
        else All tasks complete
            Sup->>U: Return complete response
        end
    end
```

## Description

Sequential execution flow showing:

**Initial Request**:
- User sends complex multi-task request to Supervisor

**Task Execution Loop**:
The supervisor repeatedly checks completion status and routes accordingly:

1. **Research Phase**:
   - If no research done → Route to Researcher
   - Researcher searches for "What is LangGraph"
   - Returns results to Supervisor

2. **Calculation Phase**:
   - If no calculation done → Route to Calculator
   - Calculator computes $1M - $700K
   - Returns $300K profit to Supervisor

3. **Summary Phase**:
   - If no summary done → Route to Summarizer
   - Summarizer generates final summary
   - Returns summary to Supervisor

4. **Completion**:
   - All tasks complete → Supervisor returns to User

**Key Pattern**: Supervisor acts as central coordinator, ensuring sequential execution and preventing infinite loops through task tracking.
