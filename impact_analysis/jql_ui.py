import streamlit as st


def render_jql_ui():

    st.subheader("JQL Query")

    jql = st.text_area(
        "Enter JQL",
        height=120,
        placeholder='project = SCRUM AND status = "Done" ORDER BY updated DESC'
    )

    return jql