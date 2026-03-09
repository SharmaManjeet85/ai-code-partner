import ollama

MODEL = "deepseek-coder:6.7b"

def review_code(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]