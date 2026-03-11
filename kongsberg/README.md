# Kongsberg

Agentic AI training material for Feb'26 — includes RAG demos (Node.js and Python), training slides, and setup scripts.

## 📁 Structure

```
kongsberg/
├── node-rag-demo/      # Node.js RAG implementation (ChromaDB + Docker)
├── py-rag-demo/        # Python RAG implementation (Chroma persistent storage)
├── slides/             # Training presentation slides
├── data/               # Training data files
├── rag-setup-js.sh     # Automated Node.js RAG setup script
├── rag-setup-py.sh     # Automated Python RAG setup script
├── main.py             # Main entry point
├── pyproject.toml      # Python project configuration
└── LICENSE             # License file
```

## Projects

| Project | Description | README |
|---------|-------------|--------|
| [Node.js RAG Demo](node-rag-demo/) | RAG with ChromaDB (Docker) + LangChain | [README](node-rag-demo/README.md) |
| [Python RAG Demo](py-rag-demo/) | RAG with Chroma persistent storage + LangChain | [README](py-rag-demo/README.md) |

## Setup Scripts

- `rag-setup-js.sh` — Automated Node.js RAG environment setup
- `rag-setup-py.sh` — Automated Python RAG environment setup

## Resources

- Training slides: `slides/`
- Course outline: `Stalwart Course Outline - AI Week - Agentic AI for Developers (6, 7 Feb).docx`
