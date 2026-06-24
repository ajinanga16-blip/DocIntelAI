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


def match_articles(
    queries,
    articles
):

    prompt = f"""
You are a Documentation Intelligence Analyst.

Queries:

{queries}

Articles:

{articles}

Return JSON only.

Format:

{{
  "matched_articles": [
    {{
      "title": "...",
      "url": "...",
      "confidence": 95,
      "reason": "..."
    }}
  ]
}}

Return only the most relevant articles.
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