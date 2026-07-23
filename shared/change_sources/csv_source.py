import streamlit as st


def render_csv_source(data):

    data["uploaded_file"] = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    return data