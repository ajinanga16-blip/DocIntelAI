import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


BUILTIN_UX_RULES = {

    "Material Design UX Writing": [

        "Use clear and concise language.",

        "Use familiar words and avoid unnecessary jargon.",

        "Make labels and actions easy to understand.",

        "Use specific action-oriented labels for buttons.",

        "Keep interface text concise while preserving meaning.",

        "Write messages that help users understand what happened.",

        "When users need to take action, explain what they should do.",

        "Use consistent terminology for the same concept.",

        "Avoid blaming or criticizing the user.",

        "Prefer language that is direct and useful to the user."

    ],

    "PatternFly UX Writing": [

        "Use clear and concise language.",

        "Write for the user's goal and task.",

        "Use direct and actionable language.",

        "Use consistent terminology.",

        "Avoid unnecessary technical jargon.",

        "Make instructions understandable and useful.",

        "Error messages should help users understand and recover.",

        "Buttons and actions should clearly communicate the result.",

        "Avoid unnecessary words and repetition.",

        "Use inclusive and user-centered language."

    ],

    "Adobe Spectrum UX Writing": [

        "Use clear and concise language.",

        "Maintain a consistent voice and terminology.",

        "Use language appropriate to the user's context.",

        "Make actions and instructions clear.",

        "Avoid unnecessary jargon.",

        "Error messages should explain the problem and help the user recover.",

        "Use specific and meaningful labels.",

        "Avoid language that blames the user.",

        "Keep interface copy concise and scannable.",

        "Use consistent terminology throughout the experience."

    ]

}


def get_builtin_rules(
    style_name
):

    return BUILTIN_UX_RULES.get(
        style_name,
        []
    )


def review_microcopy(
    microcopy_items,
    style_name,
    custom_style_content=None
):

    if not microcopy_items:

        return {

            "style_guide":
            style_name,

            "findings":
            []

        }

    rules = get_builtin_rules(
        style_name
    )

    if custom_style_content:

        custom_rules = custom_style_content

    else:

        custom_rules = ""

    prompt = f"""
You are a senior UX writing reviewer.

Review the supplied UI microcopy against the
selected UX writing style guide.

IMPORTANT:

You are reviewing MICROCOPY.

Do not redesign the UI.

Do not comment on colors, spacing, layout,
visual hierarchy, icons, or interaction design.

Do not invent product behavior.

Do not invent technical facts.

Only recommend changes when there is a meaningful
UX writing issue or improvement opportunity.

SELECTED STYLE GUIDE:

{style_name}

BUILT-IN STYLE GUIDANCE:

{json.dumps(rules, indent=2)}

CUSTOM STYLE GUIDE CONTENT:

{custom_rules}

MICROCOPY TO REVIEW:

{json.dumps(microcopy_items, indent=2)}

For every item, determine whether it should be:

- acceptable
- improvement
- issue

Use these severity values:

- low
- medium
- high

Only produce a finding when there is a meaningful
reason to change or review the copy.

For each finding return:

- text
- element_type
- approximate_context
- assessment
- recommended_text
- reason
- style_rule
- severity

Definitions:

assessment:
"acceptable", "improvement", or "issue"

recommended_text:
A concise alternative.

If the existing text is already good,
do not invent a needless alternative.

For acceptable items:

recommended_text must be null.

Return ONLY valid JSON.

Required structure:

{{
  "style_guide": "{style_name}",
  "findings": [
    {{
      "text": "Current text",
      "element_type": "button",
      "approximate_context": "Checkout form",
      "assessment": "improvement",
      "recommended_text": "Place order",
      "reason": "The action is more specific.",
      "style_rule": "Use specific action-oriented labels.",
      "severity": "medium"
    }}
  ]
}}
"""

    response = client.chat.completions.create(

        model="gpt-5",

        messages=[

            {

                "role":
                "user",

                "content":
                prompt

            }

        ]

    )

    raw_result = (
        response.choices[0]
        .message.content
    )

    #
    # Remove markdown code fences if the
    # model happens to return them.
    #

    cleaned_result = (
        raw_result
        .replace(
            "```json",
            ""
        )
        .replace(
            "```",
            ""
        )
        .strip()
    )

    try:

        return json.loads(
            cleaned_result
        )

    except json.JSONDecodeError:

        return {

            "style_guide":
            style_name,

            "findings":
            [],

            "error":
            "Unable to parse UX review response."

        }