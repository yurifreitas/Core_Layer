# ============================================================
# 🌌 CoreLayer GPT Memory System — Pipeline Runner
# ============================================================
# Autor: Yuri Freitas
# Arquitetura: Bronze → Silver → Gold → Catalog
# ============================================================

from ingestion.bronze.bronze_loader import BronzeLoader
from ingestion.silver.silver_processor import SilverProcessor
from ingestion.gold.gold_vectorizer import GoldVectorizer
from ingestion.catalog.catalog_manager import CatalogManager

def run_pipeline():
    print("🌌 Iniciando Pipeline CoreLayer GPT Memory System\n")

    catalog = CatalogManager()
    bronze = BronzeLoader()
    silver = SilverProcessor()
    gold = GoldVectorizer()

    # ============================================================
    # 1️⃣ BRONZE → SILVER → GOLD
    # ============================================================
    print("📥 Iniciando ingestão (Bronze)...")
    chunks = bronze.load_all("bronze_data")

    print("⚙️ Processando dados (Silver Layer)...")
    processed = silver.process_chunks(chunks)

    print("💾 Criando vetores (Gold Layer)...")
    index = gold.build_index(processed)

    catalog.register_embedding("knowledge_index", str(gold.index_path))
    print("✅ Catálogo atualizado:", catalog.list_summary())

    print("\n🏁 Pipeline concluído com sucesso!\n")

if __name__ == "__main__":
    run_pipeline()
