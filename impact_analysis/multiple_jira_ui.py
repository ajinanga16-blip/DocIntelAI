import streamlit as st


def render_multiple_jira_ui():

    st.subheader("Multiple JIRA Tickets")

    ticket_ids = st.text_area(
        "Enter one ticket per line",
        height=150,
        placeholder="""SCRUM-101
SCRUM-102
SCRUM-103"""
    )

    tickets = [
        ticket.strip()
        for ticket in ticket_ids.splitlines()
        if ticket.strip()
    ]

    return tickets