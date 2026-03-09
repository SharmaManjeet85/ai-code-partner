from vector_store import search_similar_code


def build_prompt(file_path, start_line, code):

    related_files = search_similar_code(code)

    context = "\n\n".join(related_files)

    prompt = f"""
You are a senior staff engineer performing a code review.

Use the repository context below to understand architecture.

REPOSITORY CONTEXT:
{context}

Review the following code and return JSON.

FORMAT:

[
  {{
    "file": "{file_path}",
    "line": "<line>",
    "issue": "<problem>",
    "suggestion": "<fix>",
    "severity": "low|medium|high"
  }}
]

Code starts at line {start_line}.

CODE:
{code}
"""

    return prompt