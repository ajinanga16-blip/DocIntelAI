from agents.jira_agent import (
    fetch_jira_ticket,
    search_jira_issues
)


def _build_ticket(ticket_id):

    jira = fetch_jira_ticket(
        ticket_id.strip()
    )

    return {

        "ticket_id": ticket_id,

        "summary": jira.get(
            "summary",
            ""
        ),

        "description": jira.get(
            "description",
            ""
        ),

        "resolution": "",

        "root_cause": "",

        "severity": "",

        "status": "",

        "module": "",

        "linked_help_article": "",

        "comments": "\n".join(
            jira.get(
                "comments",
                []
            )
        ),

        "source": "JIRA"

    }


def import_jira(
    ticket_ids=None,
    jql=None,
    sprint=None,
    epic=None
):

    tickets = []

    #
    # Convert Sprint/Epic into JQL
    #

    if sprint:
        jql = f'Sprint = "{sprint}"'

    elif epic:
        jql = f'"Epic Link" = "{epic}"'

    #
    # Run JQL search
    #

    if jql:

        ticket_ids = search_jira_issues(
            jql
        )

    #
    # Import tickets
    #

    if ticket_ids:

        for ticket_id in ticket_ids:

            tickets.append(
                _build_ticket(ticket_id)
            )

    return tickets