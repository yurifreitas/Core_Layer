from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from langchain_community.document_loaders import UnstructuredPDFLoader, TextLoader

class BronzeLoader:
    def process_file(self, path: Path):
        if path.suffix.lower() == ".pdf":
            loader = UnstructuredPDFLoader(str(path))
        else:
            loader = TextLoader(str(path))
        return loader.load()

    def load_all(self, folder: str):
        base = Path(folder)
        files = list(base.glob("*"))
        chunks = []
        with ThreadPoolExecutor(max_workers=4) as ex:
            futures = {ex.submit(self.process_file, f): f for f in files}
            for fut in as_completed(futures):
                data = fut.result()
                chunks.extend(data)
                print(f"🟤 Bronze: {futures[fut].name} ({len(data)} docs)")
        return chunks
