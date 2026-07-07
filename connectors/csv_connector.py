import pandas as pd


def import_csv(uploaded_file):

    df = pd.read_csv(uploaded_file)

    df.columns = [
        c.strip()
        for c in df.columns
    ]

    tickets = []

    for _, row in df.iterrows():

        tickets.append({

            "ticket_id": str(
                row.get("Ticket ID", "")
            ),

            "summary": str(
                row.get("Summary", "")
            ),

            "description": str(
                row.get("Description", "")
            ),

            "resolution": str(
                row.get("Support Resolution", "")
            ),

            "root_cause": str(
                row.get("Root Cause", "")
            ),

            "severity": str(
                row.get("Severity", "")
            ),

            "status": str(
                row.get("Status", "")
            ),

            "module": str(
                row.get("Module", "")
            ),

            "linked_help_article": str(
                row.get("Linked Help Article", "")
            ),

            "source": "CSV"

        })

    return tickets