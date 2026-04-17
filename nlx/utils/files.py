import subprocess
import os


def get_repo_files():
    result = subprocess.run(
        ["git", "ls-files", "--others", "--modified", "--cached"],
        capture_output=True,
        text=True
    )
    return result.stdout.splitlines()


def resolve_files(targets):
    all_files = get_repo_files()

    def normalize(path):
        return os.path.basename(path)

    resolved = [
        f for f in all_files
        if normalize(f) in targets or f in targets
    ]

    return resolved