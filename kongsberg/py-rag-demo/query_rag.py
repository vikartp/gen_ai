# file: query_rag.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PERSIST_DIR = "./chroma-store"

# 1. Re-load vector store
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

vectorstore = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embeddings,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 2. LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",  # Use OpenRouter model format: provider/model (e.g., openai/gpt-4o-mini)
    temperature=0.2,
    api_key=OPENAI_API_KEY,  # Use your OpenRouter API key here
    base_url="https://openrouter.ai/api/v1",
)

# 3. Build RAG chain using LCEL (LangChain Expression Language)
template = """Answer the question based only on the following context:
{context}

Question: {question}

Answer the question clearly and concisely based on the context provided above."""

prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Create the RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def ask(query: str):
    # Get the answer
    answer = rag_chain.invoke(query)
    
    # Get source documents separately for display
    source_docs = retriever.invoke(query)
    
    print("\nQ:", query)
    print("\nA:", answer)
    print("\nSources:")
    for i, doc in enumerate(source_docs, start=1):
        print(f"- [{i}] {doc.page_content[:120]}...")

if __name__ == "__main__":
    ask("Explain RAG to a junior backend developer.")
