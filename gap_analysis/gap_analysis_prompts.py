import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def clean_json_response(raw_text):

    raw_text = (
        raw_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return raw_text


def analyze_article(
    ticket_context,
    article
):
    """
    Analyze a support ticket against
    one documentation article.
    """

    prompt = f"""
Analyze ONLY using:

1. Ticket information
2. Existing article content

Do NOT invent product behavior.

If evidence is insufficient, state:

Additional validation required.

Return ONLY valid JSON.

{{
    "coverage_score":"",
    "confidence":"",
    "impacted_section":"",
    "impacted_step":"",
    "evidence":"",
    "gap":"",
    "recommended_change":"",
    "generated_content":""
}}

Ticket Context

Subject:
{ticket_context.get("subject","")}

Summary:
{ticket_context.get("summary","")}

Comments:
{ticket_context.get("comments","")}

Article Title

{article.get("title","")}

Article Content

{article.get("content","")}
"""

    response = client.chat.completions.create(

        model="gpt-4o",

        response_format={
            "type": "json_object"
        },

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