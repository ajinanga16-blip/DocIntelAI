from connectors.csv_connector import (
    import_csv
)

from connectors.excel_connector import (
    import_excel
)

from connectors.jira_connector import (
    import_jira
)


def import_tickets(

    source,

    uploaded_file=None,

    ticket_ids=None,

    jql=None,

    sprint=None,

    epic=None,

    release_notes=None,

    manual_input=None

):

    if source == "CSV":

        return import_csv(
            uploaded_file
        )

    if source == "Excel":

        return import_excel(
            uploaded_file
        )

    if source == "JIRA":

        return import_jira(
            ticket_ids=ticket_ids,
            jql=jql,
            sprint=sprint,
            epic=epic
        )

    if source in ["Release Notes", "Manual Input"]:

        text = (
            release_notes
            if source == "Release Notes"
            else manual_input
        ).strip()

        return [{

            "ticket_id": "TEXT-001",

            "summary": source,

            "description": text,

            "resolution": "",

            "root_cause": "",

            "severity": "",

            "status": "",

            "module": "",

            "linked_help_article": "",

            "comments": "",

            "source": source

        }]
    raise Exception(
        f"Unsupported source: {source}"
    )