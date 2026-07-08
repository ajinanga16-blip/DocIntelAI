import json

from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ai_candidate_search(
    screenshot_context,
    article_inventory,
    max_candidates=25
):
    """
    Uses GPT to shortlist the most
    relevant documentation articles.
    """

    titles = []

    for article in article_inventory:

        titles.append({

            "title":
                article["title"],

            "url":
                article["url"]

        })

    prompt = f"""
You are an expert Documentation Information Retrieval Engine.

Below is a screenshot context.

{screenshot_context}

Below is a list of documentation articles.

Return ONLY valid JSON.

{{
    "matched_articles":[
        {{
            "title":"",
            "url":"",
            "reason":""
        }}
    ]
}}

Select the {max_candidates} MOST relevant articles.

Use semantic understanding.

Examples:

SSO = Single Sign-On

Passwordless Login = Magic Link Login

Login = Authentication

Configuration = Settings

Do not explain.

Only JSON.

Articles:

{json.dumps(titles)}
"""

    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = (
        response
        .choices[0]
        .message
        .content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(result)

    except json.JSONDecodeError:

        response = client.chat.completions.create(

        model="gpt-4o",

        response_format={"type": "json_object"},

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(
        response.choices[0].message.content
    )