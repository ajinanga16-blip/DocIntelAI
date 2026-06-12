from pathlib import Path

from openai import OpenAI

from style_intelligence.style_kb_prompt import (
    STYLE_KB_GENERATION_PROMPT
)


class StyleKBGenerator:

    def __init__(self):

        self.client = OpenAI()

    def generate_style_kb(
        self,
        style_guide_content
    ):

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": STYLE_KB_GENERATION_PROMPT
                },
                {
                    "role": "user",
                    "content": style_guide_content
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content

    def save_style_kb(
        self,
        kb_content,
        output_file
    ):

        output_path = (
            Path(__file__).parent.parent
            / "style_kb"
            / output_file
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(kb_content)

        return output_path