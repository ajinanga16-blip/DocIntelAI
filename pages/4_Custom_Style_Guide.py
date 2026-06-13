import streamlit as st

from style_intelligence.customer_style_pipeline import (
    CustomerStylePipeline
)

st.title(
    "Custom Style Guide Upload"
)

style_name = st.text_input(
    "Style Guide Name"
)

input_type = st.radio(
    "Style Guide Source",
    [
        "PDF",
        "URL"
    ]
)

pipeline = (
    CustomerStylePipeline()
)

if input_type == "PDF":

    uploaded_file = st.file_uploader(
        "Upload Style Guide PDF",
        type=["pdf"]
    )

    if st.button(
        "Process PDF"
    ):

        if uploaded_file and style_name:

            file_path = (
                f"style_guides/{uploaded_file.name}"
            )

            with open(
                file_path,
                "wb"
            ) as file:

                file.write(
                    uploaded_file.getbuffer()
                )

            profile = (
                pipeline.process_pdf(
                    style_name,
                    file_path
                )
            )

            st.success(
                "Style Guide Processed"
            )

            st.json(profile)

else:

    url = st.text_input(
        "Style Guide URL"
    )

    if st.button(
        "Process URL"
    ):

        if url and style_name:

            profile = (
                pipeline.process_url(
                    style_name,
                    url
                )
            )

            st.success(
                "Style Guide Processed"
            )

            st.json(profile)