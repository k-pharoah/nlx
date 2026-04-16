from nlx.core.models import Plan, Step
import re


def extract_message(text):
    match = re.search(r"['\"](.+?)['\"]", text)
    if match:
        return match.group(1)

    if "message" in text:
        return text.split("message")[-1].strip()

    return "update"


def extract_branch(text):
    match = re.search(r"branch (?:called )?([^\s]+)", text)
    return match.group(1) if match else "feature/test"


def parse_command(command: str) -> Plan:
    cmd = command.lower()

    # normalize separators
    cmd = cmd.replace(" and ", ",")
    cmd = cmd.replace(" then ", ",")

    parts = [p.strip() for p in cmd.split(",") if p.strip()]

    steps = []

    for part in parts:
        if "stage" in part or "add" in part:
            steps.append(Step(tool="git.add_all", args={}))

        elif "commit" in part:
            steps.append(
                Step(
                    tool="git.commit",
                    args={"message": extract_message(part)}
                )
            )

        elif "push" in part:
            steps.append(Step(tool="git.push", args={}))

        elif "branch" in part:
            steps.append(
                Step(
                    tool="git.create_branch",
                    args={"name": extract_branch(part)}
                )
            )

        elif "status" in part:
            steps.append(Step(tool="git.status", args={}))

    if not steps:
        raise ValueError("Could not understand command")

    return Plan(intent="git.multi", steps=steps)