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

        files = args["files"]

        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True
        )

        all_files = result.stdout.splitlines()

        to_add = [f for f in all_files if f not in files]

        return subprocess.run(
            ["git", "add"] + to_add,
            capture_output=True,
            text=True
        )