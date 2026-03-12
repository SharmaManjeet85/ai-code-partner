import chromadb
from sentence_transformers import SentenceTransformer

# embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# persistent vector DB
client = chromadb.Client()

collection = client.get_or_create_collection("repo_code")

def index_code(file_path, chunk_id, code):

    embedding = model.encode(code).tolist()

    collection.add(
        ids=[f"{file_path}:{chunk_id}"],
        documents=[code],
        metadatas=[{"file": file_path}],
        embeddings=[embedding]
    )


def search_similar(code, top_k=3):

    embedding = model.encode(code).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    if not results["documents"]:
        return []

    return results["documents"][0]