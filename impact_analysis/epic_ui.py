import streamlit as st


def render_epic_ui():

    st.subheader("Epic")

    epic_key = st.text_input(
        "Epic Key",
        placeholder="Example: SCRUM-500"
    )

    return epic_key