# ============================================================
# 🟤 ingestion/bronze/bronze_loader.py — Versão completa
# ============================================================
# Responsável por ler e normalizar os arquivos brutos (PDFs e TXTs)
# e alimentar a camada Silver com documentos textuais.
# ============================================================

import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from langchain_community.document_loaders import UnstructuredPDFLoader, TextLoader


class BronzeLoader:
    def __init__(self, cache_path: str = "ingestion/bronze/raw_docs.json", max_workers: int = 4):
        """
        BronzeLoader — Etapa de ingestão inicial.
        - Lê PDFs e TXTs de forma paralela.
        - Tolerante a erros.
        - Salva cache para evitar reprocessamento.
        """
        self.cache_path = Path(cache_path)
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.max_workers = max_workers

    # ============================================================
    # 🔹 Processa um único arquivo (PDF ou TXT)
    # ============================================================
    def process_file(self, path: Path):
        try:
            if path.suffix.lower() == ".pdf":
                loader = UnstructuredPDFLoader(str(path))
            else:
                loader = TextLoader(str(path))
            docs = loader.load()
            print(f"🟤 Bronze: {path.name} ({len(docs)} docs)")
            return docs
        except Exception as e:
            print(f"⚠️ Erro ao processar {path.name}: {e}")
            return []

    # ============================================================
    # 🔹 Lê todos os arquivos de uma pasta em paralelo
    # ============================================================
    def load_all(self, folder: str):
        base = Path(folder)
        if not base.exists():
            raise FileNotFoundError(f"❌ Pasta '{folder}' não encontrada.")

        # Se o cache já existir, usa ele
        if self.cache_path.exists():
            print(f"🟤 Bronze: cache encontrado ({self.cache_path}), carregando...")
            with open(self.cache_path, "r") as f:
                cached = json.load(f)
            print(f"🟤 Bronze: {len(cached)} documentos carregados do cache.")
            return [{"page_content": c} for c in cached]

        files = list(base.glob("*"))
        if not files:
            raise FileNotFoundError(f"⚠️ Nenhum arquivo encontrado em {folder}")

        print(f"📥 Iniciando ingestão paralela ({len(files)} arquivos)...")

        chunks = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as ex:
            futures = {ex.submit(self.process_file, f): f for f in files}
            for fut in as_completed(futures):
                data = fut.result()
                chunks.extend(data)

        # Salva cache local
        with open(self.cache_path, "w") as f:
            json.dump([d.page_content for d in chunks], f, indent=2)

        print(f"🟤 Bronze: ingestão concluída ({len(chunks)} docs totais). Cache salvo em {self.cache_path}")
        return chunks


# ============================================================
# ✅ Execução isolada para debug
# ============================================================
if __name__ == "__main__":
    bronze = BronzeLoader(max_workers=6)
    docs = bronze.load_all("bronze_data")
    print(f"🟤 Total de documentos carregados: {len(docs)}")
