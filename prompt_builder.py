def build_prompt(file_path, code):

    prompt = f"""
You are a senior engineer reviewing code.

Review the following file and identify:

1. Bugs
2. Security issues
3. Performance problems
4. Code quality improvements
5. Best practice violations

Return results in this format:

FILE:
LINE:
ISSUE:
SUGGESTION:
SEVERITY:

Code to review:

{code}
"""

    return prompt