import re
import streamlit as st


def render_procedure(
    workflow_name,
    workflow_text
):

    st.markdown("---")

    st.title(f"📘 {workflow_name}")

    st.caption(
        "AI Generated Workflow"
    )

    lines = workflow_text.splitlines()

    current_step = None
    body = []

    def flush():

        if current_step:

            with st.container(border=True):

                st.subheader(current_step)

                for item in body:

                    st.write(item)

    for line in lines:

        line = line.strip()

        #
        # Step Heading
        #

        if line.startswith("### Step"):

            flush()

            current_step = line.replace("### ", "")

            body = []

            continue

        #
        # Ignore other headings
        #

        if line.startswith("#") or line.startswith("##"):

            continue



        if line:

            body.append(
                line.replace("**", "")
            )

    flush()