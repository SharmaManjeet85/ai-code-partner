from datetime import datetime

def write_report(report):

    issues = report["issues"]

    with open("review-report.md", "w", encoding="utf-8") as f:

        f.write("# AI Code Review Report\n\n")
        f.write(f"Generated: {report['generated']}\n\n")

        for r in issues:

            # Skip invalid items
            if not isinstance(r, dict):
                f.write("### Unknown\n\n")
                f.write(f"Issue: {str(r)}\n\n")
                f.write("---\n\n")
                continue

            file = r.get("file", "unknown")
            line = r.get("line", "?")
            issue = r.get("issue", "")
            suggestion = r.get("suggestion", "")
            severity = r.get("severity", "unknown")

            f.write(f"### {file}\n\n")
            f.write(f"Line: {line}\n\n")
            f.write(f"Issue: {issue}\n\n")
            f.write(f"Suggestion: {suggestion}\n\n")
            f.write(f"Severity: {severity}\n\n")
            f.write("---\n\n")