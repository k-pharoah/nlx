from nlx.tools.git import (
    GitStatus,
    GitCreateBranch,
    GitAddAll,
    GitAddExcept,
    GitAddPattern,
    GitCommit,
    GitPush,
    GitUndoCommitKeepStaged,
    GitUnstage,
)

registry = {
    "git.status": GitStatus(),
    "git.create_branch": GitCreateBranch(),
    "git.add_all": GitAddAll(),
    "git.add_except": GitAddExcept(),
    "git.add_pattern": GitAddPattern(),   # ← NEW
    "git.commit": GitCommit(),
    "git.push": GitPush(),
    "git.undo_commit_keep_staged": GitUndoCommitKeepStaged(),
    "git.unstage": GitUnstage(),          # ← FIXED
}

empty = []