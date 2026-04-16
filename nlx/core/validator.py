from nlx.registry import registry

def validate_plan(plan):
    for step in plan.steps:
        if step.tool not in registry:
            raise ValueError(f"Unknown tool: {step.tool}")