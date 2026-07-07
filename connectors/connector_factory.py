from connectors.csv_connector import (
    import_csv
)

from connectors.excel_connector import (
    import_excel
)

from connectors.jira_connector import (
    import_jira_ticket
)


def import_tickets(

    source,

    uploaded_file=None,

    ticket_ids=None

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

        return import_jira_ticket(
            ticket_ids
        )

    raise Exception(

        f"Unsupported source: {source}"

    )