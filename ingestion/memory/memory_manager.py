import json
import uuid
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("memory/memory.json")

class MemoryManager:
    def __init__(self):
        MEMORY_FILE.parent.mkdir(exist_ok=True)
        if not MEMORY_FILE.exists():
            MEMORY_FILE.write_text(json.dumps({"short": [], "long": []}, indent=2))
        self.data = json.loads(MEMORY_FILE.read_text())

    def add(self, query, response):
        rec = {"id": str(uuid.uuid4()), "query": query, "response": response, "time": datetime.utcnow().isoformat()}
        self.data["short"].append(rec)
        if len(self.data["short"]) >= 5:
            self._summarize()
        MEMORY_FILE.write_text(json.dumps(self.data, indent=2))

    def _summarize(self):
        combined = " ".join([x["response"] for x in self.data["short"]])
        self.data["long"].append({"summary": combined, "time": datetime.utcnow().isoformat()})
        self.data["short"].clear()

    def recall(self):
        if not self.data["long"]:
            return ""
        return "\n".join([m["summary"] for m in self.data["long"][-3:]])
