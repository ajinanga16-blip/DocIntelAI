import streamlit as st


def render_publishing():

    st.title(
        "🚀 Publishing"
    )

    st.selectbox(
        "Publish Destination",
        [
            "MkDocs",
            "GitHub Pages",
            "Confluence"
        ]
    )

    st.button(
        "Publish"
    )