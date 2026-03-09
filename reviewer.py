import sys
from codescanner import scan_codebase
from prompt_builder import build_prompt
from ai_reviewer import review_code
from report_writer import write_report
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run_review(path):

    print("Scanning codebase...")

    files = scan_codebase(path)

    results = []

    for file in files:

        print(f"Reviewing {file['path']}")

        prompt = build_prompt(file["path"], file["code"])

        review = review_code(prompt)

        results.append(review)

    write_report(results)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python reviewer.py review <path>")
        sys.exit(1)

    command = sys.argv[1]
    path = sys.argv[2]

    if command == "review":
        run_review(path)