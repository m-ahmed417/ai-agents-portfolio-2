from pathlib import Path

def load_prompt(path: str | Path)->str:
    path = Path(path)
    prompt_text = path.read_text(encoding="utf-8")
    return prompt_text

    