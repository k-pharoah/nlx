from nlx.tools.git import (
    GitStatus,
    GitCreateBranch,
    GitAddAll,
    GitAddExcept,
    GitCommit,
    GitPush,
    GitUndoCommitKeepStaged
)

registry = {
    "git.status": GitStatus(),
    "git.create_branch": GitCreateBranch(),
    "git.add_all": GitAddAll(),
    "git.add_except": GitAddExcept(),
    "git.commit": GitCommit(),
    "git.push": GitPush(),
    "git.undo_commit_keep_staged": GitUndoCommitKeepStaged()
}

empty = []