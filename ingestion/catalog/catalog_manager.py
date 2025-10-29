import json
from pathlib import Path
from datetime import datetime

CATALOG_PATH = Path("ingestion/catalog/registry.json")
CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)  

class CatalogManager:
    def __init__(self):
        if not CATALOG_PATH.exists():
            CATALOG_PATH.write_text(json.dumps({"datasets": [], "embeddings": [], "prompts": []}, indent=2))
        self.data = json.loads(CATALOG_PATH.read_text())

    def _save(self):
        CATALOG_PATH.write_text(json.dumps(self.data, indent=2))

    def register_dataset(self, name, path):
        entry = {"name": name, "path": path, "timestamp": datetime.utcnow().isoformat()}
        self.data["datasets"].append(entry)
        self._save()
        print(f"📘 Dataset registrado: {name}")

    def register_embedding(self, name, path):
        entry = {"index": name, "path": path, "timestamp": datetime.utcnow().isoformat()}
        self.data["embeddings"].append(entry)
        self._save()
        print(f"💾 Índice registrado: {name}")

    def register_prompt(self, version, desc):
        entry = {"version": version, "desc": desc, "timestamp": datetime.utcnow().isoformat()}
        self.data["prompts"].append(entry)
        self._save()
        print(f"🧩 Prompt registrado: {version}")

    def list_summary(self):
        return {k: len(v) for k, v in self.data.items()}
