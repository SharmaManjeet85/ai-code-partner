import sys
from datetime import datetime

from codescanner import scan_codebase, load_files
from code_chunker import chunk_code
from prompt_builder import build_prompt
from ai_reviewer import review_code
from report_writer import write_report
from dependency_analyzer import build_dependency_graph, detect_cycles
from vector_store import search_similar
from git_utils import get_changed_files, get_pr_changed_files


def run_review(files):

    if not files:
        print("No files to review.")
        return

    print(f"Reviewing {len(files)} files")

    file_map = load_files(files)

    print("Building dependency graph...")

    graph = build_dependency_graph(file_map)

    cycles = detect_cycles(graph)

    if cycles:
        print("⚠ Circular dependencies detected:")
        for c in cycles:
            print(" -> ".join(c))
    else:
        print("No circular dependencies detected")

    issues = []

    print("Starting AI code review...")

    for file in files:

        file_path = file["path"] if isinstance(file, dict) else file

        if file_path not in file_map:
            continue

        code = file_map[file_path]

        chunks = chunk_code(code)

        deps = list(graph.edges(file_path)) if file_path in graph else []

        for chunk in chunks:

            start_line = chunk["start_line"]
            code_chunk = chunk["code"]

            # semantic RAG retrieval
            related_code = search_similar(code_chunk)

            prompt = build_prompt(
                file_path,
                start_line,
                code_chunk,
                deps,
                related_code
            )

            ai_result = review_code(prompt)

            if ai_result:
                issues.extend(ai_result)

    report = {
        "generated": str(datetime.now()),
        "issues": issues
    }

    write_report(report)

    print("Review completed")
    print("Report generated: review-report.md")


def main():

    if len(sys.argv) < 2:
        print("""
Usage:

Full repo review:
python reviewer.py review <repo_path>

Local changes review:
python reviewer.py local-review

PR review:
python reviewer.py pr-review
""")
        return

    command = sys.argv[1]

    if command == "review":

        if len(sys.argv) < 3:
            print("Please provide repo path")
            return

        repo_path = sys.argv[2]

        print("Scanning repository...")

        files = scan_codebase(repo_path)

        run_review(files)

    elif command == "local-review":

        print("Detecting local changed files...")

        files = get_changed_files()

        if not files:
            print("No local changes detected.")
            return

        for f in files:
            print("Changed:", f)

        run_review(files)

    elif command == "pr-review":

        print("Detecting PR changed files...")

        files = get_pr_changed_files()

        if not files:
            print("No PR changes detected.")
            return

        for f in files:
            print("PR change:", f)

        run_review(files)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()