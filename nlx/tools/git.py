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