import streamlit as st


def render_jira_source(data):

    jira_mode = st.radio(
        "JIRA Import",
        [
            "Single Ticket",
            "Multiple Ticket IDs",
            "JQL",
            "Sprint",
            "Epic"
        ],
        horizontal=True
    )

    if jira_mode == "Single Ticket":

        ticket = st.text_input(
            "JIRA Ticket ID",
            placeholder="Example: SCRUM-123"
        )

        if ticket:

            data["ticket_ids"] = [ticket.strip()]

    elif jira_mode == "Multiple Ticket IDs":

        tickets = st.text_area(
            "Enter one Ticket ID per line",
            height=150
        )

        if tickets:

            data["ticket_ids"] = [
                item.strip()
                for item in tickets.splitlines()
                if item.strip()
            ]

    elif jira_mode == "JQL":

        data["jql"] = st.text_area(
            "Enter JQL Query",
            height=120
        )

    elif jira_mode == "Sprint":

        data["sprint"] = st.text_input(
            "Sprint Name or ID"
        )

    elif jira_mode == "Epic":

        data["epic"] = st.text_input(
            "Epic Key"
        )

    return data