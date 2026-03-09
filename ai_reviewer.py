import ollama
import json

MODEL = "deepseek-coder:6.7b"

def review_code(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return [{
            "file": "unknown",
            "line": "?",
            "issue": content,
            "suggestion": "",
            "severity": "unknown"
        }]