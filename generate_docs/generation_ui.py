import streamlit as st

from workflows.document_generation_job import (
    run_document_generation_job
)


def render_generation_ui(
    work_items,
    document_type,
    style_guide,
    template_selection
):
    """
    Generate documentation UI.
    """

    if st.button(
        "Generate Documentation",
        width="stretch"
    ):

        if not work_items:

            st.warning(
                "Please select a source and load at least one work item."
            )

            return

        with st.spinner(
            "Generating documentation..."
        ):

            st.session_state[
                "generated_documents"
            ] = run_document_generation_job(

                "Documentation Generation",

                work_items,

                document_type,

                style_guide,

                template_selection

            )

        st.success(
            "Documentation generated successfully."
        )