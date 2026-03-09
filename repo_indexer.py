from codescanner import scan_codebase
from vector_store import store_file_embedding

def index_repository(path):

    files = scan_codebase(path)

    print("Indexing repository...")

    for file in files:

        store_file_embedding(
            file["path"],
            file["code"]
        )

        print("Indexed:", file["path"])

    print("Repository indexed successfully.")