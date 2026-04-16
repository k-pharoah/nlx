from nlx.llm.parser import parse_command

def test_parser_returns_plan():
    plan = parse_command("anything")
    assert plan.intent == "git.status"
    assert plan.steps[0].tool == "git.status"