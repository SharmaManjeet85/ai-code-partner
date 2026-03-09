from datetime import datetime

def write_report(reviews):

    with open("review-report.md", "w", encoding="utf-8") as f:

        f.write("# AI Code Review Report\n\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        for r in reviews:

            f.write(f"### {r['file']}\n\n")
            f.write(f"Line: {r['line']}\n\n")
            f.write(f"Issue: {r['issue']}\n\n")
            f.write(f"Suggestion: {r['suggestion']}\n\n")
            f.write(f"Severity: {r['severity']}\n\n")
            f.write("---\n\n")

    print("Review report generated: review-report.md")