from nlx.tools.git import (
    GitStatus,
    GitCreateBranch,
    GitAddAll,
    GitCommit,
    GitPush,
)

registry = {
    "git.status": GitStatus(),
    "git.create_branch": GitCreateBranch(),
    "git.add_all": GitAddAll(),
    "git.commit": GitCommit(),
    "git.push": GitPush(),
}