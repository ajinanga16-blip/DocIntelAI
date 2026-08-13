import os

import streamlit as st

from template_intelligence.template_upload_service import (
    TemplateUploadService
)

from style_intelligence.customer_style_pipeline import (
    CustomerStylePipeline
)


def render_template_management():

    #
    # Page Header
    #

    st.title(
        "🎨 Styles & Templates Management"
    )

    st.caption(
        "Manage the style guides and templates "
        "used across DocIntel AI."
    )

    #
    # --------------------------------------------------
    # STYLE GUIDES
    # --------------------------------------------------
    #

    st.header(
        "📖 Style Guides"
    )

    st.caption(
        "Upload custom documentation or UX writing "
        "style guides. Uploaded guides are available "
        "to the appropriate intelligence modules."
    )

    #
    # Custom Style Guide
    #

    st.subheader(
        "Custom Style Guide Upload"
    )

    style_name = st.text_input(
        "Style Guide Name",
        key="management_style_name"
    )

    input_type = st.radio(
        "Style Guide Source",
        [
            "PDF",
            "URL"
        ],
        key="management_style_source",
        horizontal=True
    )

    pipeline = (
        CustomerStylePipeline()
    )

    #
    # PDF
    #

    if input_type == "PDF":

        uploaded_file = st.file_uploader(

            "Upload Style Guide PDF",

            type=[
                "pdf"
            ],

            key="management_style_pdf"

        )

        if st.button(
            "Process PDF",
            key="management_process_pdf"
        ):

            if not style_name:

                st.warning(
                    "Please enter a Style Guide Name."
                )

            elif not uploaded_file:

                st.warning(
                    "Please upload a Style Guide PDF."
                )

            else:

                os.makedirs(
                    "style_guides",
                    exist_ok=True
                )

                file_path = (
                    f"style_guides/"
                    f"{uploaded_file.name}"
                )

                with open(
                    file_path,
                    "wb"
                ) as file:

                    file.write(
                        uploaded_file.getbuffer()
                    )

                with st.spinner(
                    "Processing style guide..."
                ):

                    profile = (
                        pipeline.process_pdf(
                            style_name,
                            file_path
                        )
                    )

                st.success(
                    "Style Guide Processed"
                )

                st.json(
                    profile
                )

    #
    # URL
    #

    else:

        url = st.text_input(
            "Style Guide URL",
            key="management_style_url"
        )

        if st.button(
            "Process URL",
            key="management_process_url"
        ):

            if not style_name:

                st.warning(
                    "Please enter a Style Guide Name."
                )

            elif not url:

                st.warning(
                    "Please enter a Style Guide URL."
                )

            else:

                with st.spinner(
                    "Processing style guide..."
                ):

                    profile = (
                        pipeline.process_url(
                            style_name,
                            url
                        )
                    )

                st.success(
                    "Style Guide Processed"
                )

                st.json(
                    profile
                )

    #
    # --------------------------------------------------
    # TEMPLATES
    # --------------------------------------------------
    #

    st.divider()

    st.header(
        "📄 Templates"
    )

    st.caption(
        "Upload and manage custom documentation templates."
    )

    service = (
        TemplateUploadService()
    )

    uploaded_template = (
        st.file_uploader(

            "Upload Template",

            type=[
                "txt"
            ],

            key="management_template_upload"

        )
    )

    if (
        uploaded_template
        and
        st.button(
            "Save Template",
            key="management_save_template"
        )
    ):

        service.save_template(
            uploaded_template
        )

        st.success(
            "Template uploaded successfully."
        )

    #
    # Available Templates
    #

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