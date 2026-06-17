import streamlit as st


def render_impact_analysis():

    st.title(
        "⚡ Impact Analysis"
    )

    st.text_input(
        "Release or Ticket ID"
    )

    st.button(
        "Run Impact Analysis"
    )