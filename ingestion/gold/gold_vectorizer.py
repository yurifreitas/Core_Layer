# ============================================================
# 🟡 ingestion/gold/gold_vectorizer.py — versão local (Ollama)
# ============================================================
# Responsável por gerar e gerenciar o índice vetorial FAISS
# a partir dos chunks processados pela camada Silver.
# ============================================================

import os
import time
from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from ingestion.catalog.catalog_manager import CatalogManager


class GoldVectorizer:
    def __init__(self):
        # Caminho base para o índice FAISS
        self.index_path = Path("ingestion/gold/knowledge_index")
        self.index_path.parent.mkdir(parents=True, exist_ok=True)

        # Configurações simbióticas
        self.embedding_mode = os.getenv("EMBED_MODE", "ollama")  
        self.ollama_model = os.getenv("OLLAMA_EMBED_MODEL", "embeddinggemma")
        self.catalog = CatalogManager()

    # ============================================================
    # 🔹 Carregar índice existente (cache FAISS)
    # ============================================================
    def load_existing_index(self, embeddings):
        if self.index_path.exists():
            try:
                print(f"🟡 Gold: índice existente encontrado em {self.index_path}, carregando...")
                index = FAISS.load_local(
                    str(self.index_path),
                    embeddings,
                    allow_dangerous_deserialization=True
                )
                print("✅ Gold: índice carregado do cache FAISS.")
                return index
            except Exception as e:
                print(f"⚠️ Erro ao carregar índice existente: {e}")
        return None

    # ============================================================
    # 🔹 Construir índice vetorial (FAISS)
    # ============================================================
    def build_index(self, chunks):
        print(f"🧩 Usando modo de embeddings: {self.embedding_mode}")

        # Inicializa embeddings locais via Ollama
        embeddings = OllamaEmbeddings(model=self.ollama_model)

        # Verifica cache existente
        existing_index = self.load_existing_index(embeddings)
        if existing_index:
            return existing_index

        print(f"🟡 Gold: criando novo índice vetorial com modelo '{self.ollama_model}'...")
        start_time = time.time()

        # Cria FAISS a partir dos documentos
        index = FAISS.from_documents(chunks, embeddings)
        index.save_local(str(self.index_path))

        elapsed = time.time() - start_time
        print(f"🟡 Gold: índice vetorial salvo em {self.index_path} ({len(chunks)} chunks, {elapsed:.2f}s)")

        # Atualiza o catálogo simbiótico
        self.catalog.register_embedding("knowledge_index", str(self.index_path))
        print("💾 Índice registrado no catálogo.")

        return index


# ============================================================
# ✅ Execução isolada para debug
# ============================================================
if __name__ == "__main__":
    import json
    from ingestion.silver.silver_processor import SilverProcessor

    silver = SilverProcessor()
    gold = GoldVectorizer()

    # Carrega chunks do cache Silver
    chunks_path = Path("ingestion/silver/chunks.json")
    if chunks_path.exists():
        chunks = [{"page_content": c} for c in json.loads(chunks_path.read_text())]
    else:
        print("⚠️ Nenhum cache Silver encontrado. Execute primeiro a etapa Silver.")
        chunks = []

    if chunks:
        gold.build_index(chunks)
