from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def analyze_cluster_impact(
    screenshot_change,
    cluster_name,
    articles
):

    prompt = f"""
You are a Documentation Impact Analyst.

Screenshot Change:

{screenshot_change}

Cluster:

{cluster_name}

Articles:

{articles}

Generate:

Impact Summary

What Changed

What To Add

What To Remove

Recommended Documentation Updates
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

    return (
        response
        .choices[0]
        .message
        .content
    )