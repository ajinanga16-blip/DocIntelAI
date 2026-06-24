import streamlit as st

from generate_docs.template_selector_ui import (
    render_template_selector
)

from generate_docs.style_selector_ui import (
    render_style_selector
)

from generate_docs.manual_generation import (
    render_manual_generation
)

from generate_docs.jira_generation import (
    render_jira_generation
)


def render_generate_docs():

    st.title(
        "📝 Generate Documentation"
    )

    source_type = st.radio(
        "Source Type",
        [
            "Manual Input",
            "JIRA Ticket"
        ]
    )

    document_type = st.selectbox(
        "Document Type",
        [
            "User Guide",
            "FAQ",
            "Release Notes",
            "Knowledge Base",
            "Quick Start Guide",
            "Video Script",
            "Solution Article",
            "API Guide"
        ]
    )

    template_selection = (
        render_template_selector(
            document_type
        )
    )

    style_guide = (
        render_style_selector()
    )

    if source_type == "Manual Input":

        render_manual_generation(
            document_type
        )

    else:

        render_jira_generation(
            document_type,
            style_guide,
            template_selection
        )