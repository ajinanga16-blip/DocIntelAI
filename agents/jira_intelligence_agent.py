import re


def build_structured_requirements(ticket_data):
    """
    Convert raw Jira ticket data into
    structured documentation requirements.
    """

    summary = ticket_data.get("summary", "")
    description = ticket_data.get("description", "")
    comments = ticket_data.get("comments", [])

    feature_description = description
    acceptance_criteria = []

    # Split Acceptance Criteria from Description

    if "Acceptance Criteria" in description:

        parts = description.split(
            "Acceptance Criteria",
            1
        )

        feature_description = parts[0].strip()

        ac_text = parts[1].strip()

        acceptance_criteria = [
            item.strip()
            for item in re.findall(
                r"User[^.]*\.",
                ac_text
            )
        ]

    documentation_notes = []
    implementation_notes = []

    for comment in comments:

        if "documentation" in comment.lower():

            documentation_notes.append(
                comment
            )

        else:

            implementation_notes.append(
                comment
            )

    return {
        "feature_name": summary,

        "feature_description":
            feature_description,

        "acceptance_criteria":
            acceptance_criteria,

        "documentation_notes":
            documentation_notes,

        "implementation_notes":
            implementation_notes,

        "dependencies":
            ticket_data.get(
                "linked_tickets",
                []
            ),

        "attachments":
            ticket_data.get(
                "attachments",
                []
            )
    }