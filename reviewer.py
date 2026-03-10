import sys
from datetime import datetime
from codescanner import scan_codebase,load_files
from code_chunker import chunk_code
from prompt_builder import build_prompt
from ai_reviewer import review_code
from report_writer import write_report
from dependency_analyzer import build_dependency_graph, detect_cycles


def main():

    if len(sys.argv) < 3:
        print("Usage: python reviewer.py review <repo_path>")
        return

    command = sys.argv[1]
    repo_path = sys.argv[2]

    if command != "review":
        print("Unknown command")
        return

    print("Scanning repository...")

    files = scan_codebase(repo_path)

    if not files:
        print("No source files found.")
        return

    print(f"Found {len(files)} source files")

    # Load full file contents
    file_map = load_files(files)

    print("Building dependency graph...")

    graph = build_dependency_graph(file_map)

    cycles = detect_cycles(graph)

    if cycles:
        print("⚠ Circular dependencies detected:")
        for c in cycles:
            print(" -> ".join(c))
    else:
        print("No circular dependencies found")

    issues = []

    print("Starting AI code review...")

    for file_path in files:

        if isinstance(file_path, dict):
            file_path = file_path["path"]
        else:
            file_path = file_path

        code = file_map[file_path]

        chunks = chunk_code(code)

        # Dependency info for this file
        deps = list(graph.edges(file_path))

        for chunk in chunks:

            start_line = chunk["start_line"]
            code_chunk = chunk["code"]

            prompt = build_prompt(
                file_path,
                start_line,
                code_chunk,
                deps
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


if __name__ == "__main__":
    main()