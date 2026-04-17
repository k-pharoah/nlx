from dotenv import load_dotenv
from pathlib import Path
import json

from openai import OpenAI
from nlx.core.models import Plan
from nlx.llm.prompt import SYSTEM_PROMPT

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(env_path)

client = OpenAI()


def parse_command(command: str) -> Plan:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": command}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from LLM:\n{content}")

    return Plan(**data)