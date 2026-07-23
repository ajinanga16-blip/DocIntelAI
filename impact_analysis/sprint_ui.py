import streamlit as st


def render_sprint_ui():

    st.subheader("Sprint")

    sprint_name = st.text_input(
        "Sprint Name or ID",
        placeholder="Example: Sprint 24"
    )

    return sprint_name