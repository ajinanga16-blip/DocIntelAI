import pandas as pd


def load_tickets(uploaded_file):
    """
    Load support tickets from
    CSV or Excel and normalize them
    into a common structure.
    """

    if uploaded_file.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    df.columns = [col.strip() for col in df.columns]

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

            "support_resolution": str(
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

            "keywords": []

        })

    return tickets