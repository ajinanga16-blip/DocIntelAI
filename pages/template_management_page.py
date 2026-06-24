import streamlit as st

from template_intelligence.template_upload_service import (
    TemplateUploadService
)


def render_template_management():

    st.title(
        "📄 Template Management"
    )

    service = (
        TemplateUploadService()
    )

    uploaded_file = (
        st.file_uploader(
            "Upload Template",
            type=["txt"]
        )
    )

    if (
        uploaded_file
        and
        st.button(
            "Save Template"
        )
    ):

        service.save_template(
            uploaded_file
        )

        st.success(
            "Template uploaded successfully."
        )

    st.subheader(
        "Available Templates"
    )

    templates = (
        service.get_templates()
    )

    if templates:

        for template in templates:

            st.write(
                f"• {template}"
            )

    else:

        st.info(
            "No custom templates uploaded."
        )