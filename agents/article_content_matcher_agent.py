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


def match_article_content(
    queries,
    articles
):

    prompt = f"""
You are a Documentation Intelligence Analyst.

Your job is to identify documentation articles
that are impacted by the screenshot change.

Queries:

{queries}

Articles:

{json.dumps(articles, indent=2)}

Return JSON only.

Format:

{{
    "matched_articles": [
        {{
            "title": "...",
            "url": "...",
            "confidence": 95,
            "reason": "...",
            "affected_section": "..."
        }}
    ]
}}

Only return relevant articles.
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