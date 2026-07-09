from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_workflow(
    workflow_name,
    workflow_steps
):
    """
    Generate a professional workflow
    from screenshot contexts.
    """

    prompt = f"""
    You are a Senior Lead Technical Writer.

    Generate an enterprise software procedure.

    Workflow Name:
    {workflow_name}

    Screen Context:
    {workflow_steps}

    Rules

    - Do NOT invent steps.
    - Use only the detected screen context.
    - Merge duplicate actions.
    - Keep steps concise.
    - Use imperative verbs.

    Return EXACTLY in this format:

    # {workflow_name}

    ## Purpose

    One sentence describing the goal.

    ## Procedure

    ### Step 1

    **Action**

    ...

    **Expected Result**

    ...

    ### Step 2

    **Action**

    ...

    **Expected Result**

    ...

    Repeat until complete.

    Do not output any explanation outside this structure.
    """
    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[

            {
                "role": "system",
                "content": "You are an expert Technical Writer."
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0

    )

    return response.choices[0].message.content