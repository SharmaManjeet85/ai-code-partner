import subprocess

def get_changed_files():
    result = subprocess.run(
        ["git","diff","--name-only"],
        capture_output=True,
        text=True
    )
    files = result.stdout.splitlines()
    
    return files

def get_pr_changed_files(base_branch="origin/main"):

    result = subprocess.run(
        ["git", "diff", f"{base_branch}...HEAD", "--name-only"],
        capture_output=True,
        text=True
    )

    files = result.stdout.splitlines()

    return files