import base64
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def analyze_screen(
    uploaded_file
):
    """
    Analyze a UI screenshot and extract
    visible user-facing microcopy.

    This function does NOT evaluate the copy.
    It only extracts and classifies visible text.
    """

    image_bytes = (
        uploaded_file.getvalue()
    )

    encoded_image = (
        base64.b64encode(
            image_bytes
        ).decode("utf-8")
    )

    file_type = (
        uploaded_file.type
        or "image/png"
    )

    prompt = """
You are a UX microcopy extraction assistant.

Analyze the supplied product UI screenshot.

Your task is to identify ONLY user-facing UI
microcopy that should potentially be reviewed
for UX writing quality.

Do NOT recommend changes yet.

Do NOT judge the quality of the copy yet.

Do NOT invent text that is not visible.

REVIEWABLE UI COPY

Include visible text that represents:

- Page titles
- Headings
- Navigation labels
- Tabs
- Buttons
- Form labels
- Field placeholders
- Helper text
- Tooltips
- Dialog titles
- Dialog messages
- Error messages
- Warning messages
- Success messages
- Empty-state messages
- Confirmation messages
- User-facing instructions
- User-facing status messages

DO NOT REVIEW

Exclude:

- Brand names
- Logos
- Product/company names
- User-generated record names
- Customer names
- Project names
- Analysis names
- IDs
- Numbers
- Dates
- Timestamps
- Decorative text
- Technical identifiers
- URLs
- Code
- File names
- Purely informational data values
- Badges that only display counts

IMPORTANT

A visible string such as "Contact Stitching"
may be a user-facing record name rather than
microcopy.

If it appears to be data, a record name, project
name, customer name, analysis name, or other
user-generated content, exclude it.

For each reviewable item return:

- text
- element_type
- approximate_context

Use these element_type values where possible:

- page_title
- heading
- navigation
- tab
- button
- label
- placeholder
- helper_text
- tooltip
- dialog_title
- dialog_message
- error
- warning
- success
- empty_state
- confirmation
- instruction
- status_message

Return ONLY valid JSON in this structure:

{
  "items": [
    {
      "text": "Example text",
      "element_type": "button",
      "approximate_context": "Checkout form"
    }
  ]
}

Rules:

1. Extract only text actually visible.
2. Preserve the visible wording exactly.
3. Do not rewrite the text.
4. Do not recommend alternatives.
5. Do not judge the text.
6. Exclude brand names and data values.
7. If uncertain whether something is microcopy
   or user-generated data, exclude it.
8. If there is no reviewable microcopy, return:

{
  "items": []
}
"""

    response = client.chat.completions.create(

        model="gpt-5",

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

                            "url": (
                                f"data:{file_type};"
                                f"base64,{encoded_image}"
                            )

                        }

                    }

                ]

            }

        ]

    )

    return (
        response.choices[0]
        .message.content
    )