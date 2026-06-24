import streamlit as st

from template_intelligence.custom_template_service import (
    CustomTemplateService
)


def render_template_selector(
    document_type
):

    template_source = st.radio(
        "Template Source",
        [
            "Built-in",
            "Custom"
        ]
    )

    if template_source == "Built-in":

        template_name = (
            f"{document_type} Template"
        )

        st.info(
            f"Using Template: {template_name}"
        )

        return {
            "source": "Built-in",
            "template": document_type
        }

    template_service = (
        CustomTemplateService()
    )

    templates = (
        template_service
        .get_custom_templates()
    )

    if not templates:

        st.warning(
            "No custom templates available."
        )

        return {
            "source": "Custom",
            "template": None
        }

    selected_template = (
        st.selectbox(
            "Custom Template",
            templates
        )
    )

    return {
        "source": "Custom",
        "template": selected_template
    }