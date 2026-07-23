import pandas as pd


def import_csv(uploaded_file):

    df = pd.read_csv(uploaded_file)

    df.columns = [
        c.strip()
        for c in df.columns
    ]

    #
    # Remove completely empty rows
    #

    df = df.dropna(
        how="all"
    )

    tickets = []

    for _, row in df.iterrows():

        ticket = {

            "ticket_id": str(
                row.get("Ticket ID", "")
            ).strip(),

            "summary": str(
                row.get("Summary", "")
            ).strip(),

            "description": str(
                row.get("Description", "")
            ).strip(),

            "resolution": str(
                row.get("Support Resolution", "")
            ).strip(),

            "root_cause": str(
                row.get("Root Cause", "")
            ).strip(),

            "severity": str(
                row.get("Severity", "")
            ).strip(),

            "status": str(
                row.get("Status", "")
            ).strip(),

            "module": str(
                row.get("Module", "")
            ).strip(),

            "linked_help_article": str(
                row.get("Linked Help Article", "")
            ).strip(),

            "source": "CSV"

        }

        #
        # Skip rows without a Ticket ID
        #

        if not ticket["ticket_id"] or ticket["ticket_id"].lower() == "nan":
            continue

        tickets.append(ticket)

    return tickets