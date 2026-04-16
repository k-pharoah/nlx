import typer
from nlx.llm.parser import parse_command
from nlx.core.validator import validate_plan
from nlx.core.executor import execute_plan

app = typer.Typer()

@app.command()
def run(command: str, execute: bool = False):
    plan = parse_command(command)

    typer.echo("\nPlan:")
    for i, step in enumerate(plan.steps, 1):
        typer.echo(f"{i}. {step.tool} {step.args}")

    validate_plan(plan)

    if not execute:
        typer.echo("\n[DRY RUN]")
        confirm = typer.confirm("Execute?")
        if not confirm:
            typer.echo("Aborted")
            raise typer.Exit()

    execute_plan(plan)

def main():
    app()