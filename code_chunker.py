def chunk_code(code, chunk_size=200):

    lines = code.split("\n")

    chunks = []

    for i in range(0, len(lines), chunk_size):

        chunk = "\n".join(lines[i:i + chunk_size])

        chunks.append({
            "start_line": i + 1,
            "code": chunk
        })

    return chunks