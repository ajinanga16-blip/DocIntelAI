from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

from screenshot_intelligence.prompts import (
    SCREENSHOT_ANALYSIS_PROMPT,
    SCREENSHOT_DISCOVERY_PROMPT
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_screenshot(
    image_file,
    mode="analysis"
):

    image_bytes = image_file.read()

    image_file.seek(0)

    base64_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    if mode == "discovery":

        prompt = SCREENSHOT_DISCOVERY_PROMPT

    else:

        prompt = SCREENSHOT_ANALYSIS_PROMPT

    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[
            {
                "role": "user",

                "content": [

                    {
                        "type": "text",
                        "text": prompt
                    },

                    {
                        "type": "image_url",

                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }

                ]
            }
        ]
    )

    return response.choices[0].message.content