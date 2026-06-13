import streamlit as st

from style_intelligence.customer_style_pipeline import (
    CustomerStylePipeline
)


st.title(
    "Custom Style Guide Upload"
)

uploaded_file = st.file_uploader(
    "Upload Style Guide PDF",
    type=["pdf"]
)

style_name = st.text_input(
    "Style Guide Name"
)

if st.button(
    "Process Style Guide"
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

        pipeline = (
            CustomerStylePipeline()
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