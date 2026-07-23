import streamlit as st


def render_release_notes_ui():

    st.subheader("Release Notes")

    release_notes = st.text_area(
        "Paste Release Notes",
        height=200,
        placeholder="Paste release notes or change log here..."
    )

    return release_notes