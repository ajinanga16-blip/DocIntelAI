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
    Analyze one work item against one
    documentation article for documentation impact.
    """

    prompt = f"""
You are an expert Technical Documentation Impact Analyst.

Your task is to determine how the provided change context impacts an existing documentation article.

The source of the change context may be a JIRA ticket, Release Notes, Manual Input, Product Requirements Document (PRD), meeting transcript, or another product change artifact. Treat all sources equally and base your analysis only on the information provided.

Analyze ONLY using:

1. The provided Change Context (which may come from a JIRA ticket, Release Notes, Manual Input, PRD, Transcript, or another approved source).
2. The existing documentation article.

Do NOT invent product functionality.

If the available information is insufficient, return:

Additional validation required.

Determine:

- How well the article covers the change
- Which sections are impacted
- Which procedure steps are impacted
- Whether screenshots are likely impacted
- Whether warnings, notes or prerequisites require updates
- Whether the article requires minor updates or major rewriting
- What documentation changes are required

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

Change Context

Source:
{ticket_context.get("source","Unknown")}

Subject:
{ticket_context.get("subject","")}

Summary:
{ticket_context.get("summary","")}

Description:
{ticket_context.get("description","")}

Comments:
{ticket_context.get("comments","")}

Article Title

{article.get("title","")}

Article Content

{article.get("content","")}
"""

    response = client.chat.completions.create(

        model="gpt-5",

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