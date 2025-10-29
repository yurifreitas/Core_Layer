# ============================================================
# 🌌 CoreLayer GPT Memory System
# ============================================================
# Autor: Yuri Freitas
# Arquitetura: Bronze → Silver → Gold → Catalog → Prompt → Memory → Core GPT
# ============================================================

import os
from pathlib import Path
from ingestion.bronze.bronze_loader import BronzeLoader
from ingestion.silver.silver_processor import SilverProcessor
from ingestion.gold.gold_vectorizer import GoldVectorizer
from ingestion.catalog.catalog_manager import CatalogManager
from ingestion.prompt.prompt_layer import PromptLayer
from ingestion.memory.memory_manager import MemoryManager
from core.rag_pipeline import RagPipeline

BASE_DIR = Path(__file__).parent

def main():
    print("🌌 Iniciando CoreLayer GPT Memory System\n")

    # Inicializa componentes
    catalog = CatalogManager()
    memory = MemoryManager()
    prompt_layer = PromptLayer()
    bronze = BronzeLoader()
    silver = SilverProcessor()
    gold = GoldVectorizer()
    rag = RagPipeline(memory, prompt_layer)

    # ============================================================
    # 1️⃣ INGESTÃO E REGISTRO
    # ============================================================
    print("📥 Iniciando ingestão paralela...")
    chunks = bronze.load_all("bronze_data")

    print("⚙️ Processando dados (Silver Layer)...")
    processed = silver.process_chunks(chunks)

    print("💾 Criando vetores (Gold Layer)...")
    index = gold.build_index(processed)

    catalog.register_embedding("knowledge_index", str(gold.index_path))
    print("✅ Catálogo atualizado:", catalog.list_summary())

    # ============================================================
    # 2️⃣ INTERAÇÃO SIMBIÓTICA
    # ============================================================
    print("\n🧠 Pronto para consultas simbióticas (digite 'sair' para encerrar)\n")
    while True:
        query = input("❓ Pergunta: ")
        if query.lower() in ["sair", "exit", "quit"]:
            break
        response = rag.query_with_memory(query, index)
        print(f"\n💬 Resposta: {response}\n")

if __name__ == "__main__":
    main()
