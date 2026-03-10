import os

SUPPORTED_EXTENSIONS = [".cs", ".js", ".ts", ".py", ".java"]

def load_files(files):

    file_map = {}

    for file in files:

        # if scan_repo returns dict
        if isinstance(file, dict):
            file_path = file["path"]
        else:
            file_path = file

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            file_map[file_path] = f.read()

    return file_map

def scan_codebase(path):

    files = []

    for root, dirs, filenames in os.walk(path):

        for file in filenames:

            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):

                full_path = os.path.join(root, file)

                with open(full_path, "r", encoding="utf-8") as f:
                    code = f.read()

                files.append({
                    "path": full_path,
                    "code": code
                })

    return files