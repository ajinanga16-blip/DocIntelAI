import streamlit as st


def render_excel_source(data):

    data["uploaded_file"] = st.file_uploader(
        "Upload Excel",
        type=["xlsx"]
    )

    return data