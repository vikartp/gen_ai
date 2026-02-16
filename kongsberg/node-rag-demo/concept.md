# GenAI Training - Quick Revision Guide

## Self-Supervised Learning

**Definition:** A machine learning paradigm where the model learns from unlabeled data by creating its own supervision signal from the data itself.

**Key Concept:**
- No human-labeled data needed
- The model generates labels automatically from the input data
- Learns representations by predicting part of the data from other parts

**How It Works:**
1. Take unlabeled data
2. Create a "pretext task" that generates labels automatically
3. Model learns useful patterns while solving this task
4. Transfer learned knowledge to downstream tasks

**Common Techniques:**

| Technique | Description | Example |
|-----------|-------------|---------|
| **Masked Language Modeling (MLM)** | Mask random words and predict them | BERT: "The cat [MASK] on the mat" → predict "sat" |
| **Next Token Prediction** | Predict the next word/token | GPT: "The cat sat" → predict "on" |
| **Contrastive Learning** | Learn by comparing similar vs different examples | Images of same object vs different objects |
| **Autoencoding** | Compress and reconstruct data | Encode image → decode to recreate it |

**Why It Matters for GenAI:**
- Powers pre-training of large language models (GPT, BERT, LLaMA)
- Enables learning from massive unlabeled datasets (internet text)
- Foundation for transfer learning and fine-tuning
- Cost-effective: no expensive manual labeling needed

**Real-World Impact:**
- **GPT models**: Trained by predicting next token on billions of web pages
- **BERT**: Trained by masking 15% of words and predicting them
- **Vision models**: Learn by predicting rotations, colorization, or masked patches

**Key Advantage:** Scales with data - more unlabeled data = better representations

---

## RLHF (Reinforcement Learning from Human Feedback)

**Definition:** Fine-tuning technique that uses human preferences to align AI models with desired behavior.

**Three-Step Process:**
1. **Pre-train** base model (e.g., GPT)
2. **Train reward model** - humans rank model outputs (better/worse)
3. **RL optimization** - tune model to maximize reward scores using PPO

**Key Idea:** Instead of predicting "next token," optimize for "what humans prefer"

**Why It Matters:**
- Makes models helpful, harmless, and honest
- Reduces toxic/biased outputs
- Aligns model behavior with human values

**Examples:**
- **ChatGPT**: Base GPT-3.5 → RLHF → conversational assistant
- **Claude**: Constitutional AI uses RLHF principles
- **Gemini**: Aligned using human feedback

**Trade-off:** Better alignment but requires human labelers and is computationally expensive

---

## Perceptron

**Definition:** The simplest form of a neural network - a single-layer binary classifier (1957, Frank Rosenblatt).

**How It Works:**
```
Inputs (x₁, x₂, ..., xₙ)
    ↓
Weighted Sum: w₁x₁ + w₂x₂ + ... + wₙxₙ + bias
    ↓
Activation: If sum ≥ 0 → output 1, else → output 0
```

**Formula:** `output = 1 if (Σ wᵢxᵢ + b) ≥ 0 else 0`

**Learning:** Adjusts weights based on errors using gradient descent

**Limitation:** Can only learn **linearly separable** patterns (e.g., AND, OR but NOT XOR)

**Historical Importance:**
- Foundation of modern neural networks
- Led to multi-layer perceptrons (MLPs) and deep learning
- Inspired activation functions (ReLU, sigmoid, tanh)

**Modern Relevance:** Single neuron = perceptron; stack millions → deep neural networks

---

## Foundation Models vs LLMs

**Foundation Model (FM):**
- **Broad concept**: Large-scale models trained on massive unlabeled data
- **Multi-modal**: Can handle text, images, audio, video, code
- **General purpose**: One model, many downstream tasks
- **Examples**: CLIP (text+image), Whisper (audio), GPT-4V (vision+text), Gemini (multimodal)

**Large Language Model (LLM):**
- **Subset of FMs**: Specialized in language/text processing only
- **Text-only**: Trained on text corpora
- **Examples**: GPT-3.5, Claude, LLaMA, BERT, PaLM

**Key Difference:**
```
Foundation Models (Broader Category)
    ├── LLMs (Text-only)
    │   ├── GPT-3.5
    │   └── Claude
    ├── Vision Models
    │   └── Stable Diffusion
    └── Multimodal Models
        └── GPT-4V, Gemini
```

**Simple Rule:**
- **All LLMs are foundation models**
- **Not all foundation models are LLMs** (e.g., DALL-E is FM but not LLM)

**Why "Foundation"?**
These models serve as a **foundation** for building specialized applications through fine-tuning, prompting, or RAG - rather than training from scratch.

---

## How Models Get Trained

**Training Loop (4 Steps):**

```
1. Forward Pass         2. Calculate Loss       3. Backpropagation      4. Update Weights
   Input → Model           Compare prediction      Compute gradients       Adjust parameters
   → Prediction            with true label        for each weight         using optimizer
                           → Loss value           ← gradient flow          ← learning rate
       ↓                        ↓                        ↓                       ↓
   "cat image"            Predicted: dog          ∂Loss/∂w₁ = 0.05        w₁ = w₁ - α × gradient
      ↓                   Actual: cat             ∂Loss/∂w₂ = -0.12       (α = learning rate)
   Model outputs          Loss = High ❌          ... for all weights
   "dog" (wrong!)         
```

**Repeat for thousands/millions of examples → Model learns patterns**

**Key Components:**

| Component | Purpose | Example |
|-----------|---------|---------|
| **Loss Function** | Measures how wrong predictions are | Cross-entropy, MSE |
| **Optimizer** | Updates weights to reduce loss | Adam, SGD |
| **Backpropagation** | Calculates gradients efficiently | Chain rule through layers |
| **Learning Rate** | Controls step size of updates | 0.001, 0.0001 |
| **Batch Size** | Number of examples per update | 32, 64, 128 |
| **Epochs** | Full passes through dataset | 10, 100, 1000 |

**Training Phases for LLMs:**
1. **Pre-training**: Learn language patterns from massive text (self-supervised)
2. **Fine-tuning**: Adapt to specific tasks with labeled data
3. **RLHF** (optional): Align with human preferences

**Stopping Condition:** Stop when validation loss stops improving (early stopping) or after fixed epochs.

---

## LLM vs AI Agent

**LLM (Large Language Model):**
- **What it is**: A trained neural network that generates text
- **Core Function**: Takes Natural Language (NL) in → Gives Natural Language (NL) out
- **Capability**: Takes input → produces output (stateless)
- **Behavior**: Responds to prompts, no autonomous action
- **Example**: "Explain quantum physics" → GPT-4 generates explanation
- **Think of it as**: A smart parrot that predicts what to say next

**AI Agent:**
- **What it is**: A system that uses LLM(s) + tools to achieve goals autonomously
- **Capability**: Takes goal → plans steps → executes actions → adapts
- **Behavior**: Makes decisions, calls tools, maintains state across interactions
- **Example**: "Book cheapest flight to Paris" → searches flights, compares prices, books ticket
- **Think of it as**: A personal assistant that takes action

**Key Differences:**

| Aspect | LLM | AI Agent |
|--------|-----|----------|
| **Autonomy** | None - just generates text | Yes - takes actions |
| **Tools** | No external tools | Can use APIs, databases, calculators |
| **Planning** | Single response | Multi-step reasoning |
| **State** | Stateless (forgets after response) | Maintains context/memory |
| **Goal** | Answer questions | Accomplish tasks |

**Architecture:**
```
LLM:           Input → LLM → Output

AI Agent:      Goal → Planning (LLM)
                        ↓
                  Action Selection
                        ↓
               ┌────────┴────────┐
               ↓                 ↓
           Tool Call         LLM Reasoning
               ↓                 ↓
           Get Result    →  Next Action?
               ↓                 ↓
           Task Done      OR  Loop Back
```

**Example Flow:**
- **LLM**: "What's 456 × 789?" → "360,384" (may hallucinate)
- **Agent**: "What's 456 × 789?" → Calls calculator tool → Returns "359,784" (accurate)

**Real Use Cases:**
- **LLM**: ChatGPT answering coding questions
- **Agent**: AutoGPT writing code, running tests, fixing bugs automatically

---

## Context Engineering

**Definition:** The practice of structuring and optimizing the context (information) provided to an LLM to get better outputs.

**Why It Matters:**
LLMs have limited context windows (4K-200K tokens) and their performance depends heavily on what information you provide and how you structure it.

**Key Techniques:**

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **System Prompts** | Set role/behavior at start | Define assistant personality/constraints |
| **Few-Shot Examples** | Provide 2-5 input-output examples | Show format or reasoning pattern |
| **Chain-of-Thought (CoT)** | Include step-by-step reasoning | Complex problem-solving tasks |
| **RAG** | Retrieve relevant docs dynamically | Needs external/updated knowledge |
| **Context Pruning** | Remove irrelevant information | Hitting token limits |
| **Structured Output** | Specify JSON/XML format | Need parseable responses |

**Context Structure Best Practices:**
```
1. System Message (instructions/role)
2. Relevant Context (retrieved docs, data)
3. Examples (if needed)
4. User Query (clear, specific)
```

**Example - Poor vs Good Context:**

❌ **Poor:**
```
User: Fix the bug
```

✅ **Good:**
```
System: You are a Python debugging expert.

Context:
- File: auth.py, Line 45
- Error: KeyError: 'user_id'
- Function: get_user_session()

Code:
def get_user_session():
    return session['user_id']

Task: Explain the bug and provide a fix with error handling.
```

**Context Window Limits:**
- GPT-3.5: 16K tokens (~12K words)
- GPT-4: 8K-128K tokens
- Claude 3: 200K tokens
- Gemini 1.5 Pro: 1M tokens

**Pro Tip:** More context ≠ better; focus on **relevant, well-structured** context over quantity.

---

## Agentic AI vs AI Agent

**Agentic AI:**
- **What it is**: A paradigm/field of AI focused on autonomous decision-making
- **Scope**: Broad concept encompassing principles, frameworks, and approaches
- **Focus**: Building systems that can act with agency (independence, goal-orientation)
- **Think of it as**: The philosophy/science of creating autonomous AI systems

**AI Agent:**
- **What it is**: A specific implementation/system built using Agentic AI principles
- **Scope**: Concrete software application
- **Focus**: An actual working system that performs tasks autonomously
- **Think of it as**: The product/application resulting from Agentic AI research

**Simple Analogy:**
```
Agentic AI : AI Agent
    =
Robotics : Robot
    =
Computer Science : Computer Program
```

**Key Difference:**

| Aspect | Agentic AI | AI Agent |
|--------|------------|----------|
| **Type** | Research field/paradigm | Implementation/system |
| **Level** | Conceptual | Practical |
| **Example** | "Study of goal-driven systems" | "ChatGPT with function calling" |
| **Usage** | "Working on Agentic AI research" | "Built an AI agent for customer support" |

**In Practice:**
- **Agentic AI** = The principles and techniques (planning, tool use, memory, feedback loops)
- **AI Agent** = The actual system you deploy (e.g., coding agent, travel booking agent, customer service bot)

**Both Terms Often Used Interchangeably** in casual conversation, but technically Agentic AI is the umbrella concept.

---

## Chain of Thought (CoT)

**Definition:** A prompting technique that encourages LLMs to show step-by-step reasoning before giving final answers.

**How It Works:**
Instead of jumping to conclusions, the model "thinks aloud" through intermediate steps.

**Example:**

❌ **Without CoT:**
```
Q: Roger has 5 tennis balls. He buys 2 more cans of 3 balls each. How many balls does he have?
A: 11 balls
```

✅ **With CoT:**
```
Q: Roger has 5 tennis balls. He buys 2 more cans of 3 balls each. How many balls does he have?
A: Let me think step by step:
1. Roger starts with 5 balls
2. He buys 2 cans with 3 balls each
3. That's 2 × 3 = 6 new balls
4. Total: 5 + 6 = 11 balls
```

**Prompting Patterns:**

| Pattern | Prompt Addition | When to Use |
|---------|----------------|-------------|
| **Zero-Shot CoT** | "Let's think step by step..." | General reasoning tasks |
| **Few-Shot CoT** | Provide examples with reasoning | Domain-specific problems |
| **Structured CoT** | "Break this into steps: 1), 2), 3)" | Complex multi-stage tasks |

**Benefits:**
- Improves accuracy on math, logic, reasoning tasks
- Makes LLM's logic transparent and debuggable
- Reduces hallucinations by forcing systematic thinking

**Trade-offs:**
- Uses more tokens (longer responses)
- Slower response time
- May over-explain simple questions

**Pro Tip:** Add "Show your work" or "Think step-by-step" to prompts for better reasoning.

---

## Fine-Tuning

**Definition:** Training a pre-trained model on a specific dataset to adapt it for a particular task or domain.

**Process:**
```
Pre-trained Model (general knowledge)
        ↓
+ Your Custom Dataset (task-specific examples)
        ↓
Fine-Tuned Model (specialized for your use case)
```

**When to Fine-Tune:**
- Model needs to mimic specific style/tone
- Domain-specific jargon or knowledge
- Consistent output format required
- Prompt engineering isn't enough

**Types of Fine-Tuning:**

| Type | Description | Cost | Use Case |
|------|-------------|------|----------|
| **Full Fine-Tuning** | Update all model weights | High | Complete task adaptation |
| **LoRA** (Low-Rank Adaptation) | Update small adapter layers | Medium | Efficient specialization |
| **Prompt Tuning** | Learn optimal prompt embeddings | Low | Task-specific prompting |

**Example Use Cases:**
- Customer support: Fine-tune on company's help docs and tone
- Medical: Fine-tune on clinical notes and terminology
- Code: Fine-tune on internal codebase patterns
- Legal: Fine-tune on legal documents and citations

**Fine-Tuning vs Alternatives:**

| Approach | Cost | Data Needed | Update Frequency |
|----------|------|-------------|------------------|
| **Prompt Engineering** | Free | None | Instant |
| **RAG** | Low | Any documents | Real-time |
| **Fine-Tuning** | Medium-High | 100-10K examples | Periodic |

**Requirements:**
- Dataset: 100-1000+ quality examples (input-output pairs)
- Format: JSONL with prompt-completion pairs
- Compute: GPU hours (or use API like OpenAI, AWS SageMaker)

**Example Dataset:**
```json
{"prompt": "Summarize this bug report:", "completion": "Issue: Login fails..."}
{"prompt": "Summarize this bug report:", "completion": "Bug: API timeout..."}
```

**Trade-offs:**
- ✅ Better task performance, consistent outputs
- ❌ Requires labeled data, compute cost, can't update easily

**Modern Trend:** Use RAG for knowledge, fine-tuning for behavior/style.

---

## Guardrails

**Definition:** Safety mechanisms and constraints applied to LLM inputs/outputs to prevent harmful, biased, or inappropriate content.

**Why Needed:**
- LLMs can generate toxic, biased, or dangerous content
- May leak sensitive information (PII, credentials)
- Can hallucinate false information confidently
- Might follow malicious instructions (jailbreaking)

**Types of Guardrails:**

| Type | What It Does | Example |
|------|--------------|---------|
| **Input Validation** | Screen user prompts before LLM | Block prompt injections, toxic requests |
| **Output Filtering** | Check LLM responses before showing | Remove PII, profanity, harmful advice |
| **Content Moderation** | Classify content safety levels | Flag hate speech, violence, sexual content |
| **Rate Limiting** | Prevent abuse through throttling | Max 100 requests/minute per user |
| **Semantic Guardrails** | Ensure responses stay on-topic | Reject off-domain queries |

**Implementation Approaches:**

**1. Rule-Based Guardrails:**
```python
# Simple keyword blocking
banned_words = ['password', 'credit card', 'kill']
if any(word in response.lower() for word in banned_words):
    return "I cannot provide that information."
```

**2. Model-Based Guardrails:**
- Use separate classifier models (e.g., OpenAI Moderation API, Perspective API)
- Check toxicity scores before showing output

**3. Prompt-Based Guardrails:**
```
System: You are a helpful assistant. Never provide:
- Medical/legal advice
- Instructions for illegal activities
- Personal information about individuals
- Biased or discriminatory content
```

**Popular Tools:**
- **AWS Bedrock Guardrails**: Content filters, denied topics, PII redaction
- **NeMo Guardrails** (NVIDIA): Programmable rails for LLM apps
- **Guardrails AI**: Python library for structured output validation
- **LangChain Moderations**: Built-in content filtering chains

**Real-World Example:**
```python
from guardrails import Guard

guard = Guard.from_string(
    validators=["toxic-language", "pii-detection"],
    on_fail="filter"
)

# LLM response gets validated
validated_output = guard.validate(llm_response)
```

**Trade-offs:**
- ✅ Safer, compliant outputs; reduces legal/ethical risks
- ❌ May over-filter legitimate content; adds latency

**Best Practice:** Layer multiple guardrails (input + output + semantic) for robust protection.

---

## Spec-Driven Development

**Definition:** A software development methodology where you write detailed specifications (specs) first, then implement code to match those specifications.

**Core Principle:** "Specification → Implementation → Validation"

**Workflow:**
```
1. Write Specification
   ↓
   (Define inputs, outputs, behavior, constraints)
   ↓
2. Implement Code
   ↓
   (Build features matching the spec)
   ↓
3. Validate Against Spec
   ↓
   (Test that implementation meets spec)
```

**Specification Types:**

| Type | What It Defines | Example |
|------|----------------|---------|
| **API Spec** | Endpoints, request/response format | OpenAPI/Swagger |
| **Functional Spec** | What the system should do | "Login returns JWT token" |
| **Technical Spec** | How it should work | "Use bcrypt for hashing" |
| **Test Spec** | Expected behavior scenarios | Given-When-Then format |

**Example - API Spec (OpenAPI):**
```yaml
paths:
  /users/{id}:
    get:
      summary: Get user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
```

**Benefits:**
- Clear contract between teams (frontend/backend)
- Automated code generation from specs
- Early detection of design issues
- Living documentation that stays updated
- Easier testing (verify against spec)

**GenAI Connection:**
LLMs excel at spec-driven development:
```
Prompt: "Implement this API spec using FastAPI"
→ LLM generates code matching the specification
→ Validates output structure against schema
```

**Popular Tools:**
- **OpenAPI/Swagger**: REST API specifications
- **GraphQL Schema**: GraphQL API specs
- **Protocol Buffers (protobuf)**: gRPC service definitions
- **JSON Schema**: Data validation specs

**Spec-Driven vs Test-Driven (TDD):**

| Aspect | Spec-Driven | TDD |
|--------|-------------|-----|
| **Start with** | Specification document | Test cases |
| **Focus** | Contract/interface | Behavior verification |
| **Scope** | API design, architecture | Unit/function level |

**GitHub Copilot & Spec-Driven Development:**

GitHub Copilot accelerates spec-driven workflows by:

1. **Spec-to-Code Generation:**
   - Paste OpenAPI/GraphQL spec → Copilot generates compliant implementation
   - Automatically creates models, routes, validators from schema

2. **Intelligent Autocomplete:**
   - Understands spec context in comments
   - Suggests code that matches defined types and constraints

3. **Spec Validation:**
   - Generates test cases from specifications
   - Creates type-safe interfaces (TypeScript, Python type hints)

**Example Workflow:**
```python
# Spec: GET /users/{id} returns User object with id, name, email
# Copilot generates:

@app.get("/users/{id}")
async def get_user(id: int) -> User:
    user = await db.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404)
    return User(id=user.id, name=user.name, email=user.email)
```

**Benefits with Copilot:**
- Reduces boilerplate from specs to working code
- Maintains consistency between spec and implementation
- Speeds up API development by 40-60%
- Auto-generates documentation comments from spec

**Best Practice:** Combine both - write specs for architecture, TDD for implementation.

---

## Multimodal LLMs

**Definition:** Large language models that can process and generate multiple types of data (modalities) beyond just text - including images, audio, video, and code.

**Traditional LLM vs Multimodal LLM:**

| Aspect | Traditional LLM | Multimodal LLM |
|--------|----------------|----------------|
| **Input** | Text only | Text + Images + Audio + Video |
| **Output** | Text only | Text + Images + Audio |
| **Example** | GPT-3.5, BERT | GPT-4V, Gemini, Claude 3 |
| **Training** | Text corpora | Mixed data: text, images, videos |

**Common Modality Combinations:**

```
Text + Vision (Most Common)
   ├── Image Understanding (describe, analyze, OCR)
   ├── Image Generation (DALL-E, Stable Diffusion)
   └── Visual Question Answering

Text + Audio
   ├── Speech-to-Text (Whisper)
   ├── Text-to-Speech (ElevenLabs)
   └── Audio Analysis

Text + Video
   ├── Video Understanding
   ├── Video Generation (Sora)
   └── Frame-by-frame analysis
```

**Major Multimodal Models:**

| Model | Modalities | Capabilities |
|-------|-----------|-------------|
| **GPT-4V** | Text + Vision | Image analysis, OCR, diagram understanding |
| **Gemini 1.5** | Text + Image + Video + Audio | Long context (1M tokens), video understanding |
| **Claude 3** | Text + Vision | Document analysis, charts, screenshots |
| **DALL-E 3** | Text → Image | High-quality image generation |
| **Whisper** | Audio → Text | Speech recognition, transcription |
| **Sora** | Text → Video | Video generation from descriptions |

**Use Cases:**

**1. Vision + Text:**
```
Input: [Image of handwritten math problem]
Prompt: "Solve this equation"
Output: "The equation is 2x + 5 = 13, solving: x = 4"
```

**2. Document Analysis:**
```
Input: [Screenshot of dashboard]
Prompt: "What issues do you see?"
Output: "The error rate spiked at 3 PM, suggesting a deployment issue"
```

**3. Image Generation:**
```
Input: "A serene mountain landscape at sunset"
Output: [Generated image]
```

**4. Multimodal RAG:**
- Store text + images in vector DB
- Retrieve relevant visuals with text answers
- Example: Technical docs with diagrams

**How They Work:**

```
Input Processing:
   Text Input → Text Encoder → Embeddings
   Image Input → Vision Encoder → Embeddings
   Audio Input → Audio Encoder → Embeddings
        ↓
   Combined Embeddings → Transformer → Output
```

**Training Approach:**
1. **Contrastive Learning**: Align text and image embeddings (CLIP)
2. **Unified Architecture**: Single model processes all modalities
3. **Cross-Modal Attention**: Learn relationships between modalities

**Advantages:**
- Richer understanding through multiple data types
- Better context for complex tasks (e.g., UI design from screenshot)
- More natural human-AI interaction

**Limitations:**
- Higher computational cost
- More complex prompt engineering
- Potential for cross-modal hallucinations
- Larger context windows needed

**Practical Example - Kiro IDE:**
- Drop UI design image → generates matching code
- Whiteboard photo → implements architecture
- Error screenshot → diagnoses and fixes issue

**Future Trend:** Moving toward "any-to-any" models that seamlessly convert between all modalities.

---
