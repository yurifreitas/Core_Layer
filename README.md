### 🌌 CoreLayer GPT Memory System

A **symbiotic system** for ingestion, memory, and contextual reasoning built on the **Medallion Architecture** pattern — designed to create a **living, self-evolving AI**, with independent layers for ingestion, vectorization, memory, and reasoning.

---

## 🧠 Overview

The **CoreLayer GPT Memory System** organizes AI cognition into **symbolic processing and memory layers**.  
It follows the **Bronze → Silver → Gold → Catalog → Prompt → Memory → Core** model, forming a self-expanding pipeline that reads, understands, stores, and reasons over real data in real time.

---

## 🧩 General Architecture

🟤 BRONZE — Raw data ingestion  
⚪ SILVER — Semantic processing and cleaning  
🟡 GOLD — Vectorization and knowledge indexing  
🔵 CATALOG — Universal index and cognitive governance  
🟢 PROMPT — Intent control and versioning  
🟣 MEMORY — Symbiotic short- and long-term memory  
⚫ CORE — Contextual GPT reasoning (RAG)  
🔴 OBSERVABILITY — Metrics, logs, and cognitive audit  

---

## 📂 Folder Structure

```bash
corelayer/
│
├── main.py                        # Symbiotic orchestration core
│
├── core/
│   └── rag_pipeline.py             # Reasoning and retrieval pipeline (RAG)
│
├── ingestion/
│   ├── bronze/bronze_loader.py     # Parallel ingestion and data loading
│   ├── silver/silver_processor.py  # Text splitting and semantic cleaning
│   ├── gold/gold_vectorizer.py     # Vectorization (embeddings + FAISS)
│   ├── catalog/catalog_manager.py  # Universal index (datasets, prompts, vectors)
│   ├── prompt/prompt_layer.py      # Prompt versioning and templates
│   ├── memory/memory_manager.py    # Symbiotic short- and long-term memory
│   └── observability/              # (in progress) monitoring and metrics
│
└── README.md                       # This document
```
---

## ⚙️ Requirements

### 🔧 Main Dependencies
- Python ≥ 3.10  
- LangChain ≥ 0.2  
- Ollama (for local model inference)  
- FAISS  
- dotenv (optional)  

Recommended installation:
```bash
pip install langchain langchain-openai langchain-community faiss-cpu
```

Create a directory with your initial ingestion files:
```bash
mkdir bronze_data
cp /path/to/your/files/*.pdf bronze_data/
```

---

## 🚀 Run

Start the system:
```bash
python3 main.py
```

The full symbiotic pipeline will execute:

- Bronze → load and read documents  
- Silver → process and chunk text  
- Gold → embed and index vectors  
- Catalog → register dataset and embeddings  
- Core → interactive reasoning with memory  

---

## 🧩 Core Components

### 🟤 BronzeLoader
Loads all PDF and TXT files in parallel and converts them into LangChain documents.

### ⚪ SilverProcessor
Cleans and splits the content into semantically meaningful text chunks.

### 🟡 GoldVectorizer
Generates embeddings (via Ollama or Azure) and builds a persistent FAISS vector index.

### 🔵 CatalogManager
Maintains a complete registry of datasets, embeddings, prompts, and memory records.

### 🟢 PromptLayer
Manages and versions prompts, allowing domain-specific intent evolution.

### 🟣 MemoryManager
Stores recent interactions (short-term) and automatically generates long-term summaries.

### ⚫ RagPipeline
Combines memory, vector retrieval, and GPT/Ollama reasoning into contextualized, evolving responses.

---

## 🧑‍💻 Author

**Yuri Freitas**  
Developer and researcher in **symbiotic AI architectures**, cognitive memory systems, and self-evolving reasoning pipelines.
