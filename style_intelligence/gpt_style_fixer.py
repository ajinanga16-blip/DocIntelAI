from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class GPTStyleFixer:

    def fix_passive_voice(
        self,
        sentence
    ):

        prompt = f"""
Rewrite the following sentence using active voice.

Return only the corrected sentence.

Sentence:
{sentence}
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
            .strip()
        )

    def shorten_sentence(
        self,
        sentence
    ):

        prompt = f"""
Rewrite the following sentence into 2 or more shorter sentences.

Requirements:
- Maximum 20 words per sentence
- Improve readability
- Keep the meaning unchanged

Return only the rewritten text.

Sentence:
{sentence}
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
            .strip()
        )