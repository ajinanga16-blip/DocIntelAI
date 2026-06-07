from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_documentation(
    feature_description,
    document_type
):

    prompt = f"""
You are an expert Technical Writer.

Follow the instructions exactly.

Use the required structure and headings exactly as provided.

Do not rename headings.

Do not omit sections.

Generate markdown output.

{feature_description}
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

    return response.choices[0].message.content