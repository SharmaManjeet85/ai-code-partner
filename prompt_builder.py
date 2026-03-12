from ast_parser import extract_structure


def build_prompt(file_path, start_line, code, deps=None, related_code=None):

    structure = extract_structure(file_path, code)

    ast_context = f"""
Classes: {structure['classes']}
Methods: {structure['methods']}
"""

    dependency_context = ""

    if deps:
        dependency_context = f"""
Dependencies:
{deps}
"""

    related_context = ""

    if related_code:
        related_context = "\nRELATED REPOSITORY CODE:\n"

        for c in related_code:
            related_context += c[:500] + "\n---\n"

    prompt = f"""
You are a senior staff engineer performing a code review.

FILE: {file_path}

AST STRUCTURE:
{ast_context}

{dependency_context}

{related_context}

Review the following code and identify issues.

Return ONLY JSON in this format:

[
  {{
    "file": "{file_path}",
    "line": "<line>",
    "issue": "<problem>",
    "suggestion": "<fix>",
    "severity": "low|medium|high"
  }}
]

CODE STARTING AT LINE {start_line}

{code}

IMPORTANT:
Return ONLY valid JSON.
Do not include explanations.
Do not include markdown.
Do not include text outside JSON.
Return only JSON.
"""

    return prompt



