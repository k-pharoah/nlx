import subprocess
from nlx.tools.base import Tool

class GitStatus(Tool):
    name = "git.status"

    def execute(self, args):
        return subprocess.run(
            ["git", "status"],
            capture_output=True,
            text=True
        )