# GenAI Projects

This repository contains multiple AI and RAG (Retrieval-Augmented Generation) projects, including Node.js and Python implementations, PDF parsing utilities, and agentic AI experiments.

## 📁 Project Structure

```
GenAI/
├── kongsberg/              # RAG demos and training materials
│   ├── node-rag-demo/      # Node.js RAG implementation
│   ├── py-rag-demo/        # Python RAG implementation
│   └── slides/             # Training slides
├── pdf-parser/             # PDF text extraction utility
├── agentic-ai/             # Agentic AI experiments
└── README.md               # This file
```

## 🚀 Quick Start Guide

### Prerequisites

- **Node.js** (v18 or higher)
- **Python** (3.10 or higher)
- **Docker** (for ChromaDB server - Node.js demo only)
- **API Keys**: OpenAI or OpenRouter API key

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd GenAI
```

### 2. Set Up Environment Variables

Each project includes a `.env.example` file as a template. Copy it to `.env` and add your actual API keys:

**For Node.js RAG Demo:**
```bash
cd kongsberg/node-rag-demo
cp .env.example .env
# Then edit .env and replace 'your-api-key-here' with your actual API key
```

**For Python RAG Demo:**
```bash
cd kongsberg/py-rag-demo
cp .env.example .env
# Then edit .env and replace 'your-api-key-here' with your actual API key
```

**For Agentic AI:**
```bash
cd agentic-ai
cp .env.example .env
# Then edit .env and replace 'your-api-key-here' with your actual API key
```

**On Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
# Then edit .env in your text editor
```

> **Note**: You can use either OpenAI API keys or OpenRouter API keys. Both projects are configured to work with OpenRouter.
> 
> **Security**: The `.env` file (with real keys) is gitignored and will NOT be committed. Only `.env.example` (with placeholders) is tracked in Git.

---

## 🔧 Project-Specific Setup

### A. Node.js RAG Demo (`kongsberg/node-rag-demo`)

This demo uses ChromaDB with a Docker container and LangChain.

#### Setup Steps:

1. **Install Dependencies:**
   ```bash
   cd kongsberg/node-rag-demo
   npm install
   ```

2. **Start ChromaDB Server (Docker):**
   ```bash
   docker run -d -p 8000:8000 chromadb/chroma
   ```
   
   Or use the automated setup script:
   ```bash
   cd kongsberg
   bash rag-setup-js.sh
   ```

3. **Build the Vector Index:**
   ```bash
   node build-index.mjs
   ```

4. **Query the RAG System:**
   ```bash
   node query-rag.mjs
   ```

#### Key Files:
- `build-index.mjs` - Creates vector embeddings and stores them in ChromaDB
- `query-rag.mjs` - Queries the RAG system
- `package.json` - Node.js dependencies

---

### B. Python RAG Demo (`kongsberg/py-rag-demo`)

This demo uses Chroma's persistent storage (no Docker needed) and LangChain.

#### Setup Steps:

1. **Create Virtual Environment:**
   ```bash
   cd kongsberg/py-rag-demo
   python -m uv venv
   ```

2. **Activate Virtual Environment:**
   - **Windows:** `.venv\Scripts\activate`
   - **Linux/Mac:** `source .venv/bin/activate`

3. **Install UV (if not already installed):**
   ```bash
   pip install uv
   ```
   Alternative options
   # Uninstall pip version if present
   pip uninstall uv -y

   # Install properly
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   -> follow terminal guide after this

4. **Install Dependencies:**
   ```bash
   python -m uv pip install langchain-openai langchain-chroma langchain langchain-text-splitters python-dotenv --python .venv\Scripts\python.exe
   ```
   
   Or use the automated setup script:
   ```bash
   cd kongsberg
   bash rag-setup-py.sh
   ```

5. **Build the Vector Index:**
   ```bash
   python build_index.py
   ```

6. **Query the RAG System:**
   ```bash
   python query_rag.py
   ```

#### Key Files:
- `build_index.py` - Creates vector embeddings and stores them in Chroma
- `query_rag.py` - Queries the RAG system using LCEL (LangChain Expression Language)

---

### C. PDF Parser (`pdf-parser`)

A utility for extracting text from PDF files, including rotated text.

#### Setup Steps:

1. **Create Virtual Environment:**
   ```bash
   cd pdf-parser
   python -m venv venv
   ```

2. **Activate Virtual Environment:**
   - **Windows:** `venv\Scripts\activate`
   - **Linux/Mac:** `source venv/bin/activate`

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Parser:**
   ```bash
   python pdf_parser.py <path-to-pdf-file>
   ```

5. **Run Tests:**
   ```bash
   pytest test_pdf_parser.py
   ```

#### Key Files:
- `pdf_parser.py` - Main PDF parsing script
- `requirements.txt` - Python dependencies
- `test_pdf_parser.py` - Unit tests

---

### D. Agentic AI (`agentic-ai`)

Experimental agentic AI implementations.

#### Setup Steps:

1. **Create Virtual Environment:**
   ```bash
   cd agentic-ai
   uv venv
   ```

2. **Activate Virtual Environment:**
   - **Windows:** `.venv\Scripts\activate`
   - **Linux/Mac:** `source .venv/bin/activate`

3. **Install Dependencies:**
   ```bash
   uv pip install -e .
   ```
   Or if uv installed properly and having pyproject.toml(preferred)
   ```bash
   uv sync
   ```
   Or if there's a requirements file:
   ```bash
   uv pip install -r requirements.txt
   ```

---

## 🔑 API Keys Configuration

Both RAG demos support **OpenAI** and **OpenRouter** APIs:

### Using OpenAI:
```env
OPENAI_API_KEY=sk-...your-openai-key...
```

### Using OpenRouter:
```env
OPENAI_API_KEY=sk-or-v1-...your-openrouter-key...
```

The code is configured to use OpenRouter's base URL (`https://openrouter.ai/api/v1`) by default. You can modify model names in the source files:

- **Node.js**: `build-index.mjs`, `query-rag.mjs`
- **Python**: `build_index.py`, `query_rag.py`

Available OpenRouter model examples:
- `openai/gpt-4o-mini`
- `anthropic/claude-3-5-sonnet`
- `google/gemini-pro`

---

## 🗂️ What Gets Regenerated

After cloning the repo, these files/folders will be regenerated:

| Item | Generated By | Purpose |
|------|--------------|---------|
| `.env` | Copy from `.env.example` | API keys and secrets (real values) |
| `node_modules/` | `npm install` | Node.js dependencies |
| `.venv/` | `python -m venv` or `uv venv` | Python virtual environments |
| `chroma_data/` | `build-index.mjs` | Node.js vector database |
| `chroma-store/` | `build_index.py` | Python vector database |
| `__pycache__/` | Python runtime | Python bytecode cache |

---

## 📚 Additional Resources

### Kongsberg Training Materials
- Training slides are in `kongsberg/slides/`
- Course outline: `kongsberg/Stalwart Course Outline - AI Week - Agentic AI for Developers (6, 7 Feb).docx`

### Setup Scripts
- `kongsberg/rag-setup-js.sh` - Automated Node.js RAG setup
- `kongsberg/rag-setup-py.sh` - Automated Python RAG setup

---

## 🧪 Testing

### PDF Parser Tests:
```bash
cd pdf-parser
pytest test_pdf_parser.py
```

---

## 📝 Notes

- Vector databases (`chroma_data/`, `chroma-store/`) are NOT committed to Git - must be regenerated
- Environment files (`.env`) with real API keys are NOT committed to Git
- Template files (`.env.example`) ARE committed to Git as examples
- Generated text files (`*_extracted.txt`) are NOT committed to Git
- Lock files (`uv.lock`, `package-lock.json`) may or may not be committed depending on your team's preference
- After cloning, copy `.env.example` to `.env` in each project and add your real API keys

---

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Ensure all tests pass
4. Submit a pull request

---

## 📄 License

See `kongsberg/LICENSE` for details.

---

## 🆘 Troubleshooting

### Issue: ChromaDB connection error (Node.js)
**Solution**: Ensure Docker container is running:
```bash
docker run -d -p 8000:8000 chromadb/chroma
```

### Issue: ModuleNotFoundError in Python
**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
.venv\Scripts\activate
python -m uv pip install <missing-package>
```

### Issue: OpenAI API rate limits
**Solution**: Consider using OpenRouter for access to multiple LLM providers with better rate limits.

---

## 📧 Contact

For questions or issues, please open an issue in the repository.
