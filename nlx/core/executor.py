from nlx.registry import registry

def execute_plan(plan):
    for step in plan.steps:
        tool = registry[step.tool]

        print(f"\n→ {step.tool}")
        result = tool.execute(step.args)

        if result.stdout:
            print(result.stdout)

        if result.stderr:
            print("ERR:", result.stderr)

        if result.returncode != 0:
            print("Step failed. Stopping.")
            break