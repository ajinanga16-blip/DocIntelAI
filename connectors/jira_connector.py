from agents.jira_agent import (
    fetch_jira_ticket
)


def import_jira_ticket(
    ticket_ids
):
    """
    Import one or more JIRA tickets
    into the common ticket model.
    """

    tickets = []

    for ticket_id in ticket_ids:

        jira = fetch_jira_ticket(
            ticket_id.strip()
        )

        tickets.append({

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

        })

    return tickets