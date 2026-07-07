import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_article_metadata(
    title,
    url,
    content
):
    """
    Extract searchable metadata.

    The article content is NOT stored.
    Only metadata is saved.
    """

    prompt = f"""
You are a Documentation Intelligence Engine.

Extract ONLY valid JSON.

{{
    "description":"",
    "category":"",
    "features":[],
    "tasks":[],
    "ui_elements":[],
    "error_topics":[],
    "keywords":[]
}}

Title

{title}

URL

{url}

Article

{content[:12000]}
"""

    print("=" * 60)
    print("AI Metadata Extraction")
    print(title)
    print(f"Content Length: {len(content)}")
    print("=" * 60)

    response = client.chat.completions.create(

        model="gpt-4o-mini",

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