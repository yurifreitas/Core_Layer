import json
from pathlib import Path

PROMPT_DIR = Path("ingestion/prompts")

class PromptLayer:
    def __init__(self):
        PROMPT_DIR.mkdir(exist_ok=True)

    def get_prompt(self, version="default"):
        p = PROMPT_DIR / f"{version}.json"
        if not p.exists():
            return {"system": "Você é uma IA simbiótica com raciocínio contextual.", "temperature": 0.2}
        return json.loads(p.read_text())

    def save_prompt(self, version, data):
        p = PROMPT_DIR / f"{version}.json"
        p.write_text(json.dumps(data, indent=2))
        print(f"🧠 Prompt salvo: {version}")
