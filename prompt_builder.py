from vector_store import search_similar_code
from ast_parser import extract_structure

def build_prompt(file_path, start_line, code):

    structure = extract_structure(code)

    ast_context = f"""
Classes: {structure['classes']}
Methods: {structure['methods']}
"""

    prompt = f"""
You are a senior staff engineer performing a code review.

Understand the structure of the code before reviewing.

FILE: {file_path}

AST STRUCTURE:
{ast_context}

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

CODE STARTS AT LINE {start_line}

CODE:
{code}

IMPORTANT:
Return only JSON.
"""

    return prompt