# ============================================================
# 🧠 ingestion/memory/memory_manager.py — Versão expandida
# ============================================================
# - Armazena memórias curtas e longas
# - Agrupa mensagens em threads
# - Resume automaticamente ao longo do tempo
# ============================================================

import json
import uuid
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("ingestion/memory/memory.json")


class MemoryManager:
    def __init__(self):
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        if not MEMORY_FILE.exists():
            MEMORY_FILE.write_text(json.dumps({"threads": {}, "sessions": []}, indent=2))
        self.data = json.loads(MEMORY_FILE.read_text())

        # Sessão atual
        self.current_session = str(uuid.uuid4())
        self.data["sessions"].append({
            "id": self.current_session,
            "started": datetime.utcnow().isoformat(),
            "threads": []
        })

    # ============================================================
    # 🔹 Adiciona uma nova interação à memória
    # ============================================================
    def add(self, query, response, thread_id=None):
        if not thread_id:
            thread_id = str(uuid.uuid4())

        rec = {
            "id": str(uuid.uuid4()),
            "query": query,
            "response": response,
            "time": datetime.utcnow().isoformat()
        }

        # Adiciona à thread
        if thread_id not in self.data["threads"]:
            self.data["threads"][thread_id] = {"messages": [], "summary": ""}
            self.data["sessions"][-1]["threads"].append(thread_id)

        self.data["threads"][thread_id]["messages"].append(rec)

        # Auto-sumarização simbiótica
        if len(self.data["threads"][thread_id]["messages"]) >= 5:
            self._summarize_thread(thread_id)

        self._save()

        return thread_id

    # ============================================================
    # 🔹 Resume automaticamente as respostas de uma thread
    # ============================================================
    def _summarize_thread(self, thread_id):
        msgs = self.data["threads"][thread_id]["messages"]
        combined = " ".join([m["response"] for m in msgs])
        summary = f"Resumo simbiótico ({datetime.utcnow().isoformat()}):\n{combined[:800]}..."
        self.data["threads"][thread_id]["summary"] = summary
        # Mantém só as últimas 5 mensagens
        self.data["threads"][thread_id]["messages"] = msgs[-5:]

    # ============================================================
    # 🔹 Recupera memórias recentes e contextuais
    # ============================================================
    def recall(self, limit_threads=3):
        threads = list(self.data["threads"].values())
        recent = threads[-limit_threads:] if threads else []
        context = ""
        for t in recent:
            if t["summary"]:
                context += t["summary"] + "\n"
            for msg in t["messages"]:
                context += f"Q: {msg['query']}\nA: {msg['response']}\n"
        return context.strip()

    # ============================================================
    # 🔹 Salva a memória no disco
    # ============================================================
    def _save(self):
        MEMORY_FILE.write_text(json.dumps(self.data, indent=2))

    # ============================================================
    # 🔹 Finaliza a sessão atual (gera resumo simbiótico global)
    # ============================================================
    def close_session(self):
        session = self.data["sessions"][-1]
        thread_ids = session.get("threads", [])
        summaries = [self.data["threads"][tid]["summary"] for tid in thread_ids if self.data["threads"][tid]["summary"]]
        global_summary = " ".join(summaries) if summaries else ""
        session["ended"] = datetime.utcnow().isoformat()
        session["summary"] = global_summary[:2000] + "..." if global_summary else ""
        self._save()
        print(f"🧩 Sessão {self.current_session[:8]} encerrada e registrada.")


# ============================================================
# 🔍 Execução isolada para debug
# ============================================================
if __name__ == "__main__":
    mem = MemoryManager()
    tid = mem.add("Qual o sentido da vida?", "O sentido é criar significado.")
    mem.add("E Jung?", "Jung acreditava na individuação.", thread_id=tid)
    print(mem.recall())
    mem.close_session()
