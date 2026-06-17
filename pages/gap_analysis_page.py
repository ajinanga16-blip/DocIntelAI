import streamlit as st


def render_gap_analysis():

    st.title(
        "🔍 Knowledge Gap Analysis"
    )

    st.file_uploader(
        "Upload Support Ticket CSV"
    )

    st.button(
        "Analyze"
    )