from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(env_path)

from nlx.core.models import Plan
from openai import OpenAI
import json

client = OpenAI()

SYSTEM_PROMPT = """
You convert natural language into a JSON execution plan.

Allowed tools:
- git.status()
- git.create_branch(name: string)
- git.add_all()
- git.add_except(files: string[])
- git.commit(message: string)
- git.push()

Rules:
- Output ONLY valid JSON
- No explanations
- Use exact tool names
- Always return: { "intent": string, "steps": [...] }

Examples:

Input: "undo last commit but keep changes staged"
Output:
{
  "intent": "git.undo",
  "steps": [
    {"tool": "git.undo_commit_keep_staged", "args": {}}
  ]
}

Input: "stage all, commit with message 'test', push"
Output:
{
  "intent": "git.multi",
  "steps": [
    {"tool": "git.add_all", "args": {}},
    {"tool": "git.commit", "args": {"message": "test"}},
    {"tool": "git.push", "args": {}}
  ]
}

Input: "stage all except app.py and config.json"
Output:
{
  "intent": "git.multi",
  "steps": [
    {
      "tool": "git.add_except",
      "args": {"files": ["app.py", "config.json"]}
    }
  ]
}
"""

def parse_command(command: str) -> Plan:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": command}
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from LLM:\n{content}")

    return Plan(**data)