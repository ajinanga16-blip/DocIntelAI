import pandas as pd
import streamlit as st

from connectors.connector_factory import (
    import_tickets
)


def render_work_item_loader():

    ticket_source = st.selectbox(

        "Work Item Source",

        [
            "CSV",
            "Excel",
            "JIRA"
        ]

    )

    uploaded_file = None
    ticket_ids = None

    if ticket_source == "CSV":

        uploaded_file = st.file_uploader(

            "Upload CSV",

            type=["csv"]

        )

    elif ticket_source == "Excel":

        uploaded_file = st.file_uploader(

            "Upload Excel",

            type=["xlsx"]

        )

    else:

        jira_mode = st.radio(

            "JIRA Import",

            [

                "Single Ticket",

                "Multiple Ticket IDs",

                "JQL (Coming Soon)",

                "Sprint (Coming Soon)",

                "Epic (Coming Soon)"

            ],

            horizontal=True

        )

        if jira_mode == "Single Ticket":

            ticket = st.text_input(

                "Ticket ID"

            )

            if ticket:

                ticket_ids = [ticket]

        elif jira_mode == "Multiple Ticket IDs":

            ticket_text = st.text_area(

                "Ticket IDs (One Per Line)"

            )

            if ticket_text:

                ticket_ids = [

                    item.strip()

                    for item in ticket_text.splitlines()

                    if item.strip()

                ]

    if not uploaded_file and not ticket_ids:

        return []

    tickets = import_tickets(

        source=ticket_source,

        uploaded_file=uploaded_file,

        ticket_ids=ticket_ids

    )

    st.success(

        f"Loaded {len(tickets)} work item(s)."

    )

    table = []

    for ticket in tickets:

        table.append({

            "ID": ticket.get("ticket_id", ""),

            "Severity": ticket.get("severity", ""),

            "Module": ticket.get("module", ""),

            "Status": ticket.get("status", ""),

            "Summary": ticket.get("summary", "")

        })

    st.dataframe(

        pd.DataFrame(table),

        width="stretch"

    )

    st.info(

        "Each work item will be analyzed independently."

    )

    return tickets