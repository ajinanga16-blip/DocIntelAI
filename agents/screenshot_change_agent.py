from openai import OpenAI
from dotenv import load_dotenv

import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def summarize_screenshot_change(
    comparison_result
):

    prompt = f"""
You are a Documentation Impact Analyst.

Comparison Result:

{comparison_result}

Return JSON only.

Format:

{{
  "change_summary": "...",

  "added_elements": [
    "..."
  ],

  "removed_elements": [
    "..."
  ],

  "modified_elements": [
    "..."
  ],

  "navigation_changes": [
    {{
      "old_path": "...",
      "new_path": "..."
    }}
  ],

  "documentation_impact_summary": "..."
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = (
        response
        .choices[0]
        .message
        .content
    )

    # Remove markdown fences if GPT adds them

    content = (
        content
        .replace(
            "```json",
            ""
        )
        .replace(
            "```",
            ""
        )
        .strip()
    )

    return json.loads(
        content
    )