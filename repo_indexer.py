from codescanner import scan_codebase, load_files
from code_chunker import chunk_code
from vector_store import index_code
import sys

def index_repository(repo_path):

    print("Scanning repository...")

    files = scan_codebase(repo_path)

    file_map = load_files(files)

    print("Indexing repository for semantic search...")

    for file_path, code in file_map.items():

        chunks = chunk_code(code)

        for i, chunk in enumerate(chunks):

            index_code(file_path, i, chunk["code"])

    print("Repository indexing completed")

def main():

     if len(sys.argv) < 2:
        print("Usage: python repo_indexer.py <repo_path>")
        return

repo_path = sys.argv[1]

index_repository(repo_path)


if __name__ == "__main__":
    main()