from nlx.registry import registry

def execute_plan(plan):
    for step in plan.steps:
        tool = registry[step.tool]
        result = tool.execute(step.args)

        if result.returncode != 0:
            print("Error:", result.stderr)
            break
        else:
            print(result.stdout)