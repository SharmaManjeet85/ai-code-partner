import sys
from concurrent.futures import ThreadPoolExecutor
from codescanner import scan_codebase
from code_chunker import chunk_code
from prompt_builder import build_prompt
from ai_reviewer import review_code
from report_writer import write_report


def review_file(file):

    reviews = []

    chunks = chunk_code(file["code"])

    for chunk in chunks:

        prompt = build_prompt(
            file["path"],
            chunk["start_line"],
            chunk["code"]
        )

        result = review_code(prompt)

        reviews.extend(result)

    return reviews


def run_review(path):

    files = scan_codebase(path)

    all_reviews = []

    with ThreadPoolExecutor(max_workers=4) as executor:

        results = executor.map(review_file, files)

        for r in results:
            all_reviews.extend(r)

    write_report(all_reviews)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python reviewer.py review <path>")
        sys.exit(1)

    command = sys.argv[1]
    path = sys.argv[2]

    if command == "review":
        run_review(path)