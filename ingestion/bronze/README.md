━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟤 CAMADA BRONZE — Ingestão e Captura de Dados
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📥 Função: coletar e armazenar dados brutos vindos de qualquer fonte.

🔹 Origem:
  - Uploads (PDF, CSV, JSON, logs)
  - APIs externas (Genesys, WhatsApp, ERP, sensores)
  - Streams (mensagens, eventos, áudio, vídeos)
  - Observabilidade de interações (chats e fluxos de agentes)

🔧 Processos:
  - Extração
  - Normalização leve
  - Armazenamento em blob/data lake (Cloud Storage, S3, ADLS)
  - Registro inicial no catálogo de ingestão

📂 Exemplo:
bronze/
 ├── raw/
 │   ├── documentos/
 │   ├── logs/
 │   ├── uploads/
 ├── ingestion_pipeline.py
 ├── connectors/
