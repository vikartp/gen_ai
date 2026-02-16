# RAG (Retrieval-Augmented Generation) Demo

## What is RAG?

RAG combines **information retrieval** with **text generation** to give LLMs access to external knowledge. Instead of relying only on training data, the LLM retrieves relevant documents from a vector database before generating answers.

## RAG Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        INDEXING PHASE                           │
│                     (build-index.mjs)                           │
└─────────────────────────────────────────────────────────────────┘
                                │
    Raw Documents               │
    ↓                           ↓
    "Agentic AI..."         Text Splitter
    "RAG uses..."               │
    "ChromaDB..."               ↓
                           Chunks (400 chars)
                                │
                                ↓
                    OpenAI Embeddings Model
                    (text-embedding-3-large)
                                │
                                ↓
                         Vector Embeddings
                         [0.23, -0.15, ...]
                                │
                                ↓
                       ┌────────────────┐
                       │   ChromaDB     │ ← Persistent Storage
                       │ Vector Store   │   (./chroma_data)
                       └────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                         QUERY PHASE                             │
│                      (query-rag.mjs)                            │
└─────────────────────────────────────────────────────────────────┘
                                │
    User Query                  │
    ↓                           ↓
    "Explain RAG..."        Embed Query
                                │
                                ↓
                    ┌───────────────────────┐
                    │  Vector Similarity    │
                    │  Search (top-k=4)     │
                    │  in ChromaDB          │
                    └───────────────────────┘
                                │
                                ↓
                    Retrieved Relevant Docs
                                │
                                ↓
                    ┌───────────────────────┐
                    │  Build Prompt with    │
                    │  Context + Query      │
                    └───────────────────────┘
                                │
                                ↓
                    ┌───────────────────────┐
                    │   ChatGPT (GPT-4)     │
                    │   Generates Answer    │
                    └───────────────────────┘
                                │
                                ↓
                         Final Answer
```

## Demo Structure

**Two-Step Process:**

1. **Index Building** (`npm run build:index`)
   - Splits documents into chunks
   - Converts chunks to vector embeddings
   - Stores in ChromaDB

2. **Query Execution** (`npm run query:rag`)
   - Embeds user question
   - Finds similar document chunks
   - Sends context + question to LLM
   - Returns grounded answer

**Key Files:**
- `build-index.mjs` - Creates the knowledge base
- `query-rag.mjs` - Answers questions using RAG
- `chroma_data/` - Persistent vector storage

---

# ChromaDB Setup Instructions

## Method 1: Local Python Installation

Install ChromaDB via pip:

```bash
pip install chromadb
```

Run ChromaDB server locally:

```bash
chroma run --host localhost --port 8000
```

## Method 2: Docker (Recommended)

Run ChromaDB in a Docker container with persistent storage:

```bash
docker run -d -p 8000:8000 -v ./chroma_data:/data chromadb/chroma
```

**Flags:**
- `-d`: Run in detached mode (background)
- `-p 8000:8000`: Map port 8000 from container to host
- `-v ./chroma_data:/data`: Mount local directory for persistent storage

**Container Management:**

Check if container is running:
```bash
docker ps
```

Stop the container:
```bash
docker stop <container_id>
```

View logs:
```bash
docker logs <container_id>
```

---

## Learning Resources

### TensorFlow Playground
🔗 **[https://playground.tensorflow.org](https://playground.tensorflow.org)**

Interactive neural network visualizer that runs in your browser. Great for understanding:
- How neural networks learn patterns
- Effect of layers, neurons, and activation functions
- Impact of learning rate and regularization
- Visual representation of decision boundaries

**Perfect for:** Beginners wanting to see how changing network architecture affects model behavior in real-time.

### Amazon SageMaker
🔗 **[https://aws.amazon.com/sagemaker](https://aws.amazon.com/sagemaker)**

Fully managed ML platform from AWS for building, training, and deploying machine learning models at scale.

**Key Features:**
- **SageMaker Studio**: IDE for ML development
- **AutoPilot**: Automated ML model creation
- **Pre-built algorithms**: Ready-to-use ML models
- **Model training**: Distributed training on managed infrastructure
- **Deployment**: One-click model deployment with auto-scaling
- **JumpStart**: Pre-trained foundation models (LLMs, vision models)

**Use Cases:**
- Train custom models without managing infrastructure
- Deploy LLMs and generative AI models
- Fine-tune foundation models (GPT, BERT, Stable Diffusion)
- MLOps pipelines for production ML workflows

**Pricing:** Pay-as-you-go for compute, storage, and model inference

### Amazon Bedrock
🔗 **[https://aws.amazon.com/bedrock](https://aws.amazon.com/bedrock)**

Fully managed service for accessing foundation models (FMs) from leading AI companies through a single API.

**Available Models:**
- **Anthropic**: Claude 3.5 (Sonnet, Haiku, Opus)
- **Meta**: Llama 3
- **Amazon**: Titan (text, embeddings, multimodal)
- **Cohere**: Command, Embed
- **Stability AI**: Stable Diffusion

**Key Features:**
- **No infrastructure**: Serverless access to LLMs
- **Fine-tuning**: Customize models with your data
- **RAG support**: Built-in knowledge bases with vector search
- **Agents**: Create autonomous AI agents with tool calling
- **Guardrails**: Content filtering and safety controls
- **Private**: Your data isn't used to train base models

**Use Cases:**
- Build chatbots and conversational AI
- Text generation, summarization, and analysis
- Image generation with Stable Diffusion
- RAG applications with managed vector DB
- Enterprise GenAI apps with compliance needs

**Pricing:** Pay per token (input/output) - no upfront costs

### Kiro
🔗 **[https://kiro.dev](https://kiro.dev)**

AI-powered IDE and development platform built by AWS that emphasizes **spec-driven development** for building production-ready applications with AI agents.

**Core Philosophy:**
"From vibe coding to viable code" - brings structure to AI coding through executable specifications.

**Key Features:**

**1. Spec-Driven Development:**
- Converts natural language prompts → structured requirements in EARS notation
- Auto-generates architecture, system design, and tech stack
- Creates discrete tasks sequenced by dependencies

**2. Advanced AI Agents:**
- **Autopilot Mode**: Autonomous task execution without step-by-step instructions
- **Agent Hooks**: Event-triggered agents (e.g., on file save) for background tasks
- **Multimodal**: Accepts text, images, UI designs, whiteboard photos

**3. Developer Experience:**
- **CLI Access**: Work from terminal (macOS, Linux, Windows)
- **VS Code Compatible**: Import extensions, themes, and settings
- **Native MCP Support**: Connect to docs, databases, APIs
- **Smart Context Management**: Understands intent across large codebases

**4. Development Lifecycle:**
```
Prompt → Requirements (EARS) → Architecture → Tasks → Implementation → Tests
```

**Powered By:**
- **Claude Sonnet 4.5**: For advanced coding and reasoning
- **Auto Mode**: Mix of frontier models for optimal quality/cost balance

**Unique Capabilities:**
- Generate Git commit messages automatically
- Intelligent error diagnostics (syntax, type, semantic)
- Real-time code diffs with approve/edit workflow
- Per-prompt credit usage tracking
- Agent steering via configuration files

**Use Cases:**
- Rapid prototyping (concept → working prototype in days)
- Complex feature implementation on large codebases
- Automated documentation and unit test generation
- Learning new tech stacks with AI assistance
- Terraform modules, cloud infrastructure, containerization

**Testimonials Highlight:**
- "Reduced time to customer value from weeks to days"
- "Built secure file sharing app in 2 days from scratch"
- "Kiro gives structure to chaos before writing code"

**Pricing:** Credit-based system with transparent per-prompt usage

**Enterprise Features:**
- Enterprise-grade security and privacy
- Team collaboration capabilities
- Custom steering and workflows