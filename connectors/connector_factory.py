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

    manual_input=None,

    document_title=None

):

    #
    # CSV
    #

    if source == "CSV":

        return import_csv(
            uploaded_file
        )

    #
    # Excel
    #

    if source == "Excel":

        return import_excel(
            uploaded_file
        )

    #
    # JIRA
    #

    if source == "JIRA":

        return import_jira(

            ticket_ids=ticket_ids,

            jql=jql,

            sprint=sprint,

            epic=epic

        )

    #
    # Release Notes / Manual Input
    #

    if source in [
        "Release Notes",
        "Manual Input"
    ]:

        text = (

            release_notes

            if source == "Release Notes"

            else manual_input

        )

        text = (
            text or ""
        ).strip()

        #
        # Use the supplied document title.
        #
        # We intentionally do NOT use
        # "Manual Input" or "Release Notes"
        # as the document title.
        #

        title = (
            document_title or ""
        ).strip()

        #
        # Temporary fallback.
        #
        # This prevents the application from
        # producing an empty title if the
        # current UI has not yet been updated
        # to provide document_title.
        #

        if not title:

            if source == "Manual Input":

                title = "Untitled Document"

            else:

                title = "Release Notes"

        return [{

            "ticket_id":
            "TEXT-001",

            "summary":
            title,

            "description":
            text,

            "resolution":
            "",

            "root_cause":
            "",

            "severity":
            "",

            "status":
            "",

            "module":
            "",

            "linked_help_article":
            "",

            "comments":
            "",

            "source":
            source

        }]

    #
    # Unsupported source
    #

    raise Exception(

        f"Unsupported source: {source}"

    )