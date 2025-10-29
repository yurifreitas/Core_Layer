# ============================================================
# ⚪ ingestion/silver/silver_processor.py — Versão completa
# ============================================================
# Responsável por processar os documentos da camada Bronze,
# dividir em chunks semânticos e salvar em cache local.
# ============================================================

import json
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter


class SilverProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 150):
        """
        Inicializa o processador Silver (semântica intermediária)
        - chunk_size: tamanho máximo de cada trecho
        - chunk_overlap: sobreposição entre chunks para manter contexto
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.output_path = Path("ingestion/silver/chunks.json")
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    def process_chunks(self, docs):
        """
        Divide documentos em chunks semânticos reutilizáveis
        e salva resultado em arquivo JSON para cache incremental.
        """
        # Se o cache já existir, reaproveita
        if self.output_path.exists():
            print(f"⚪ Silver: cache existente encontrado ({self.output_path}), carregando...")
            with open(self.output_path, "r") as f:
                cached = json.load(f)
            print(f"⚪ Silver: {len(cached)} chunks carregados do cache.")
            return [{"page_content": c} for c in cached]

        # Caso contrário, processa e salva
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

        chunks = splitter.split_documents(docs)
        serialized = [c.page_content for c in chunks]

        # Salva para reutilização futura
        with open(self.output_path, "w") as f:
            json.dump(serialized, f, indent=2)

        print(f"⚪ Silver: {len(chunks)} chunks gerados e salvos em {self.output_path}")
        return chunks


# ============================================================
# ✅ Uso de exemplo (isolado)
# ============================================================
if __name__ == "__main__":
    from ingestion.bronze.bronze_loader import BronzeLoader

    bronze = BronzeLoader()
    silver = SilverProcessor()

    docs = bronze.load_all("bronze_data")
    chunks = silver.process_chunks(docs)
    print(f"⚪ Total final de chunks: {len(chunks)}")
