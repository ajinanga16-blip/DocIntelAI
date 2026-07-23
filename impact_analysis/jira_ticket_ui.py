import streamlit as st


def render_jira_ticket_ui():

    st.subheader("JIRA Ticket")

    ticket_id = st.text_input(
        "JIRA Ticket ID",
        placeholder="Example: SCRUM-123"
    )

    return ticket_id