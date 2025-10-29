# ============================================================
# ⚫ core/rag_pipeline.py — versão local (Ollama, compatível LC 0.3+)
# ============================================================
from ollama import chat

class RagPipeline:
    def __init__(self, memory, prompt_layer, model="llama3.2"):
        self.memory = memory
        self.prompt_layer = prompt_layer
        self.model = model

    def query_with_memory(self, query, index):
        # 🔹 Recupera prompt e memória
        prompt = self.prompt_layer.get_prompt("default")
        recall = self.memory.recall()

        # 🔹 Busca contexto nos vetores FAISS
        retriever = index.as_retriever(search_kwargs={"k": 3})

        # ✅ Compatível com LangChain >= 0.3
        try:
            docs = retriever.invoke(query)
        except AttributeError:
            # fallback p/ versões antigas
            docs = retriever._get_relevant_documents(query)

        context = "\n".join([d.page_content for d in docs]) + "\n" + recall

        # 🔹 Monta a mensagem completa
        messages = [
            {
                "role": "system",
                "content": prompt.get(
                    "system",
                    "Você é uma IA simbiótica local com raciocínio contextual.",
                ),
            },
            {
                "role": "user",
                "content": f"Pergunta: {query}\n\nContexto:\n{context}",
            },
        ]

        # 🔹 Chama o modelo local Ollama
        response = chat(model=self.model, messages=messages)

        # 🔹 Extrai o texto da resposta
        result = response["message"]["content"]

        # 🔹 Atualiza a memória simbiótica
        self.memory.add(query, result)

        return result
