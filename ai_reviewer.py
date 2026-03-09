import ollama
import json
import re

MODEL = "deepseek-coder:6.7b"

def extract_json(text):

    match = re.search(r'\[.*\]', text, re.DOTALL)

    if match:
        return match.group(0)

    return None


def review_code(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    json_part = extract_json(content)

    if json_part:
        try:
            return json.loads(json_part)
        except:
            pass

    return [{
        "file": "unknown",
        "line": "?",
        "issue": content,
        "suggestion": "",
        "severity": "unknown"
    }]