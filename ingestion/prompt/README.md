━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟢 CAMADA PROMPT LAYER — Linguagem e Intenção
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 Função: versionar e controlar prompts, intenções e contextos de raciocínio.

🔹 Componentes:
  - Regras de prompt (por domínio, persona, tarefa)
  - Templates e versionamento
  - Controle de temperatura, estilo e formato de resposta
  - Histórico de evolução de prompts (fine-tuning simbiótico)

📂 Exemplo:
prompt_layer/
 ├── prompts/
 │   ├── products_v2.yaml
 │   ├── support_intent_v1.yaml
 ├── intent_registry.py
 ├── prompt_optimizer.py
