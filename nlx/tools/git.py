import subprocess
from nlx.tools.base import Tool

class GitStatus(Tool):
    name = "git.status"

    def execute(self, args):
        return subprocess.run(["git", "status"], capture_output=True, text=True)


class GitCreateBranch(Tool):
    name = "git.create_branch"

    def execute(self, args):
        return subprocess.run(
            ["git", "checkout", "-b", args["name"]],
            capture_output=True,
            text=True
        )


class GitAddAll(Tool):
    name = "git.add_all"

    def execute(self, args):
        return subprocess.run(["git", "add", "."], capture_output=True, text=True)


class GitCommit(Tool):
    name = "git.commit"

    def execute(self, args):
        return subprocess.run(
            ["git", "commit", "-m", args["message"]],
            capture_output=True,
            text=True
        )


class GitPush(Tool):
    name = "git.push"

    def execute(self, args):
        return subprocess.run(["git", "push"], capture_output=True, text=True)
    

class GitAddExcept(Tool):
    name = "git.add_except"

    def execute(self, args):
        import subprocess
        import os

        exclude_files = set(args["files"])

        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True
        )

        all_files = result.stdout.splitlines()

        # normalize to just filenames
        def normalize(path):
            return os.path.basename(path)

        to_add = [
            f for f in all_files
            if normalize(f) not in exclude_files
        ]

        return subprocess.run(
            ["git", "add"] + to_add,
            capture_output=True,
            text=True
        )
    
class GitUndoCommitKeepStaged(Tool):
    name = "git.undo_commit_keep_staged"

    def execute(self, args):
        import subprocess

        return subprocess.run(
            ["git", "reset", "--soft", "HEAD~1"],
            capture_output=True,
            text=True
        )