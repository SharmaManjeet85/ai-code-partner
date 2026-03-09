def build_prompt(file_path, start_line, code):

    prompt = f"""
You are a senior staff engineer reviewing code.

Analyze the following code and return ONLY valid JSON.

JSON format:

[
  {{
    "file": "{file_path}",
    "line": "<line number>",
    "issue": "<problem>",
    "suggestion": "<fix>",
    "severity": "low | medium | high"
  }}
]

Rules:
- Identify bugs
- Identify security problems
- Identify performance issues
- Identify code quality issues

Code starts at line {start_line}.

CODE:
{code}
"""

    return prompt