from nlx.core.models import Plan, Step

def parse_command(command: str) -> Plan:
    cmd = command.lower()

    steps = []

    if "status" in cmd:
        steps.append(Step(tool="git.status", args={}))

    if "branch" in cmd:
        name = "feature/test"
        words = cmd.split()
        if "called" in words:
            name = words[words.index("called") + 1]
        elif "branch" in words:
            idx = words.index("branch")
            if idx + 1 < len(words):
                name = words[idx + 1]

        steps.append(Step(tool="git.create_branch", args={"name": name}))

    if "stage" in cmd or "add" in cmd:
        steps.append(Step(tool="git.add_all", args={}))

    if "commit" in cmd:
        message = "update"
        if "message" in cmd:
            message = cmd.split("message")[-1].strip()
        steps.append(Step(tool="git.commit", args={"message": message}))

    if "push" in cmd:
        steps.append(Step(tool="git.push", args={}))

    if not steps:
        raise ValueError("Could not understand command")

    return Plan(intent="git.multi", steps=steps)