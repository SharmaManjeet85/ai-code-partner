from datetime import datetime

def write_report(results):

    filename = "review-report.md"

    with open(filename, "w", encoding="utf-8") as f:

        f.write("# AI Code Review Report\n\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        for result in results:
            f.write(result)
            f.write("\n\n---\n\n")

    print(f"Report generated: {filename}")