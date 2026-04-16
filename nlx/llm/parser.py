from nlx.core.models import Plan, Step

def parse_command(command: str) -> Plan:
    return Plan(
        intent="git.status",
        steps=[
            Step(tool="git.status", args={})
        ]
    )