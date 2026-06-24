from openai import OpenAI
from dotenv import load_dotenv

import os
import base64

from screenshot_intelligence.help_site_prompts import (
    HELP_SITE_IMPACT_PROMPT
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_help_site_impact(
    screenshot_file,
    site_content
):

    image_bytes = screenshot_file.read()

    base64_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text":
                            HELP_SITE_IMPACT_PROMPT
                            + "\n\n"
                            + site_content
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":
                                f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content