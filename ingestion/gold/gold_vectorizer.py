# ============================================================
# 🟡 ingestion/gold/gold_vectorizer.py — versão local (Ollama)
# ============================================================
import os
from pathlib import Path
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

class GoldVectorizer:
    def __init__(self):
        self.index_path = Path("gold/knowledge_index")
        self.index_path.parent.mkdir(parents=True, exist_ok=True)

        # Define o modo padrão
        self.embedding_mode = os.getenv("EMBED_MODE", "ollama")  

        # Nome do modelo local (pode mudar conforme o que você baixou)
        self.ollama_model = os.getenv("OLLAMA_EMBED_MODEL", "embeddinggemma")

    def build_index(self, chunks):
        print(f"🧩 Usando modo de embeddings: {self.embedding_mode}")


            # 🔹 Usa embeddings locais via Ollama
        embeddings = OllamaEmbeddings(model=self.ollama_model)

        # Cria e salva o índice FAISS
        index = FAISS.from_documents(chunks, embeddings)
        index.save_local(str(self.index_path))
        print(f"🟡 Gold: índice vetorial salvo em {self.index_path}")
        return index
