import streamlit as st


def render_download_buttons(
    result,
    txt_file_name,
    md_file_name
):

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="Download TXT",
            data=result,
            file_name=txt_file_name,
            mime="text/plain"
        )

    with col2:

        st.download_button(
            label="Download Markdown",
            data=result,
            file_name=md_file_name,
            mime="text/markdown"
        )