# 🌌 CoreLayer GPT Memory System

Sistema simbiótico de ingestão, memória e raciocínio contextual sobre o padrão **Medallion Architecture**, projetado para construir uma **IA viva e autoevolutiva**, com camadas independentes e integração completa entre ingestão, vetorização, memória e raciocínio GPT.

---

## 🧠 Visão Geral

O **CoreLayer GPT Memory System** organiza o fluxo cognitivo da IA em **camadas de processamento e memória simbiótica**.  
A arquitetura segue o modelo **Bronze → Silver → Gold → Catalog → Prompt → Memory → Core**, formando um pipeline autoexpansivo que lê, entende, armazena e raciocina sobre dados reais em tempo real.

---

## 🧩 Arquitetura Geral

🟤 BRONZE — Ingestão bruta de dados

⚪ SILVER — Processamento e limpeza semântica

🟡 GOLD — Vetorização e indexação de conhecimento

🔵 CATALOG — Índice universal e governança cognitiva

🟢 PROMPT — Controle e versionamento de intenções

🟣 MEMORY — Memória simbiótica de curto e longo prazo

⚫ CORE — Raciocínio GPT contextualizado (RAG)

🔴 OBSERVABILITY — Métricas, logs e auditoria cognitiva


---

## 📂 Estrutura de Pastas

```

corelayer/
│
├── main.py # Núcleo de orquestração simbiótica
│
├── core/
│ └── rag_pipeline.py # Pipeline de raciocínio e recuperação (RAG)
│
├── ingestion/
│ ├── bronze/bronze_loader.py # Ingestão e leitura paralela de dados
│ ├── silver/silver_processor.py # Split e limpeza de texto
│ ├── gold/gold_vectorizer.py # Vetorização (embeddings + FAISS)
│ ├── catalog/catalog_manager.py # Índice universal (datasets, prompts, vetores)
│ ├── prompt/prompt_layer.py # Versões e templates de prompts
│ ├── memory/memory_manager.py # Curto e longo prazo de memória simbiótica
│ └── observability/ # (em expansão) monitoramento e métricas
│
└── README.md # Este documento
```
---

## ⚙️ Requisitos

### 🔧 Dependências principais
- Python ≥ 3.10  
- LangChain ≥ 0.2  
- Ollama
- FAISS  
- dotenv (opcional)  

Instalação recomendada:
```bash
pip install langchain langchain-openai langchain-community faiss-cpu
```
Crie um diretório com seus arquivos para ingestão inicial:
```bash
mkdir bronze_data
cp /caminho/para/arquivos/*.pdf bronze_data/
```
🚀 Execução

Inicie o sistema:
```bash
python3 main.py
```

### 🧩 Componentes Principais
## 🟤 BronzeLoader

Lê todos os arquivos PDF e TXT de forma paralela e os transforma em documentos utilizáveis.

## ⚪ SilverProcessor

Faz limpeza semântica e divisão de conteúdo em chunks de tamanho ideal.

## 🟡 GoldVectorizer

Converte cada chunk em embeddings e cria um índice FAISS persistente.

## 🔵 CatalogManager

Mantém o registro completo de datasets, embeddings, prompts e memórias.

## 🟢 PromptLayer

Gerencia e versiona prompts, permitindo evolução de intenções por domínio.

## 🟣 MemoryManager

Armazena interações recentes (curto prazo) e gera resumos automáticos (longo prazo).

## ⚫ RagPipeline

Une memória + vetores + GPT para formar respostas contextualizadas com aprendizado contínuo.



🧑‍💻 Autor

Yuri Freitas
Desenvolvedor e pesquisador de arquiteturas simbióticas aplicadas à IA cognitiva, sistemas de memória e pipelines autoevolutivos.# Core_Layer
