━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚪ CAMADA SILVER — Processamento e Padronização
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Função: transformar, limpar e organizar os dados brutos.

🔹 Processos:
  - Deduplicação e limpeza semântica
  - Tokenização / chunking de textos
  - Extração de metadados (autor, domínio, relevância)
  - Validação sintática e semântica
  - Indexação em estrutura vetorial inicial

📦 Armazenamento:
  - Banco intermediário (CosmosDB / Firestore)
  - Vector Store temporária (FAISS, Chroma)

📂 Exemplo:
silver/
 ├── processors/
 │   ├── cleaner.py
 │   ├── chunker.py
 │   ├── validator.py
 ├── embeddings_temp/
 ├── silver_transform.py
