from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_documentation(feature_description, document_type):

    prompt = f"""
You are an expert Technical Writer.

Create a professional {document_type}.

Feature Description:

{feature_description}

Requirements:
- Clear structure
- End-user focused
- Professional tone
- Markdown format
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