# ============================================================
# ⚫ CoreLayer GPT Memory Chat — Interação Simbiótica
# ============================================================
# Usa o índice vetorial salvo (Gold) e a memória persistente
# para responder perguntas em modo simbiótico local.
# ============================================================

from pathlib import Path
from ingestion.catalog.catalog_manager import CatalogManager
from core.memory_manager import MemoryManager       # ✅ caminho correto
from core.prompt_layer import PromptLayer
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from core.rag_pipeline import RagPipeline


def start_chat():
    print("🧠 Iniciando modo simbiótico de raciocínio (local)\n")

    # ============================================================
    # 🔹 Inicializa componentes simbióticos
    # ============================================================
    catalog = CatalogManager()
    memory = MemoryManager()
    prompt_layer = PromptLayer()

    # ============================================================
    # 🔹 Carrega índice vetorial existente (FAISS)
    # ============================================================
    index_path = Path("ingestion/gold/knowledge_index")
    if not index_path.exists():
        print("❌ Nenhum índice encontrado. Execute primeiro o pipeline com `python pipeline_run.py`.")
        return

    print("🟡 Carregando índice vetorial existente...")
    embeddings = OllamaEmbeddings(model="embeddinggemma")
    index = FAISS.load_local(str(index_path), embeddings, allow_dangerous_deserialization=True)

    # Inicializa pipeline simbiótico
    rag = RagPipeline(memory, prompt_layer)

    print("\n🧠 Pronto para consultas simbióticas (digite 'sair' para encerrar)\n")

    # ============================================================
    # 🔹 Loop principal de interação simbiótica
    # ============================================================
    thread_id = None
    try:
        while True:
            query = input("❓ Pergunta: ").strip()
            if query.lower() in ["sair", "exit", "quit"]:
                print("\n🧩 Encerrando sessão simbiótica...")
                memory.close_session()
                break

            # 🔸 Executa pipeline RAG + memória
            response = rag.query_with_memory(query, index)

            # 🔸 Armazena interação simbiótica
            thread_id = memory.add(query, response, thread_id=thread_id)

            print(f"\n💬 Resposta: {response}\n")

    except KeyboardInterrupt:
        print("\n🧩 Sessão interrompida manualmente.")
        memory.close_session()


if __name__ == "__main__":
    start_chat()
