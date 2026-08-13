from connectors.connector_factory import (
    import_tickets
)


def load_work_items(source):

    #
    # CSV / Excel require a file
    #

    if source["source_type"] in [
        "CSV",
        "Excel"
    ]:

        if source["uploaded_file"] is None:

            return []

    #
    # JIRA requires some input
    #

    if source["source_type"] == "JIRA":

        if (

            not source["ticket_ids"]

            and not source["jql"]

            and not source["sprint"]

            and not source["epic"]

        ):

            return []

    #
    # Release Notes require text
    #

    if source["source_type"] == "Release Notes":

        if not source["release_notes"].strip():

            return []

    #
    # Manual Input requires text
    #

    if source["source_type"] == "Manual Input":

        if not source["manual_input"].strip():

            return []

        if not source["document_title"].strip():

            return []

    #
    # Load work items
    #

    return import_tickets(

        source=source["source_type"],

        uploaded_file=source["uploaded_file"],

        ticket_ids=source["ticket_ids"],

        jql=source["jql"],

        sprint=source["sprint"],

        epic=source["epic"],

        release_notes=source["release_notes"],

        manual_input=source["manual_input"],

        document_title=source.get(
            "document_title",
            ""
        )

    )