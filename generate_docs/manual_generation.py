import streamlit as st

from agents.content_agent import (
    generate_documentation
)


def render_manual_generation(
    document_type
):

    feature_description = st.text_area(
        "Feature Description",
        height=200
    )

    if st.button(
        "Generate Documentation"
    ):

        with st.spinner(
            "Generating documentation..."
        ):

            result = (
                generate_documentation(
                    feature_description,
                    document_type
                )
            )

        st.success(
            "Documentation generated successfully."
        )

        st.markdown(
            result
        )