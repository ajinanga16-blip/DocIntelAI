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


def classify_links(
    links
):

    prompt = f"""
You are a Documentation Intelligence Analyst.

Determine which URLs are likely documentation articles.

Keep:

- Help Articles
- KB Articles
- Documentation Pages
- User Guides
- Procedures
- FAQs

Remove:

- Home Pages
- Pricing Pages
- Contact Pages
- Careers Pages
- Product Marketing Pages
- Community Pages

Return JSON only.

Format:

{{
    "documentation_urls": [
        "...",
        "..."
    ]
}}

URLs:

{links}
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