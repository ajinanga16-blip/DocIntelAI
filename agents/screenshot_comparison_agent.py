from openai import OpenAI
from dotenv import load_dotenv

import os
import base64

from screenshot_intelligence.comparison_prompts import (
    SCREENSHOT_COMPARISON_PROMPT
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def compare_screenshots(
    old_image_file,
    new_image_file
):

    old_image_bytes = old_image_file.read()

    new_image_bytes = new_image_file.read()

    old_base64_image = base64.b64encode(
        old_image_bytes
    ).decode("utf-8")

    new_base64_image = base64.b64encode(
        new_image_bytes
    ).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": SCREENSHOT_COMPARISON_PROMPT
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": (
                                f"data:image/png;base64,"
                                f"{old_base64_image}"
                            )
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": (
                                f"data:image/png;base64,"
                                f"{new_base64_image}"
                            )
                        }
                    }
                ]
            }
        ]
    )

    return response.choices[0].message.content