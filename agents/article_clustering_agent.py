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


def cluster_articles(
    articles
):

    article_list = []

    for article in articles:

        article_list.append(
            {
                "title": article.get(
                    "title",
                    ""
                ),
                "url": article.get(
                    "url",
                    ""
                )
            }
        )

    prompt = f"""
You are a Documentation Intelligence Analyst.

Group the articles into logical clusters.

Examples:

- User Management
- User Roles
- User Administration
- FAQ
- Troubleshooting
- Configuration
- Setup
- Procedures

Return JSON only.

Format:

[
    {{
        "cluster_name": "...",
        "articles": [
            "...",
            "..."
        ]
    }}
]

Articles:

{json.dumps(article_list, indent=2)}
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

    return content