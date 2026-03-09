import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.get_or_create_collection(name="codebase")


def store_file_embedding(file_path, code):

    embedding = model.encode(code).tolist()

    collection.add(
        documents=[code],
        embeddings=[embedding],
        ids=[file_path]
    )


def search_similar_code(query, top_k=3):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results["documents"][0]