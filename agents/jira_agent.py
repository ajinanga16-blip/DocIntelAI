import os
import requests
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = (
    os.getenv("JIRA_URL")
    or os.getenv("JIRA_BASE_URL")
)

JIRA_EMAIL = os.getenv("JIRA_EMAIL")

JIRA_TOKEN = (
    os.getenv("JIRA_TOKEN")
    or os.getenv("JIRA_API_TOKEN")
)


def extract_text_from_adf(node):

    text = ""

    if isinstance(node, dict):

        if node.get("type") == "text":
            text += node.get("text", "")

        if "content" in node:
            for child in node["content"]:
                text += extract_text_from_adf(child)

    elif isinstance(node, list):

        for item in node:
            text += extract_text_from_adf(item)

    return text


def fetch_jira_ticket(ticket_id):

    url = f"{JIRA_URL}/rest/api/3/issue/{ticket_id}"

    response = requests.get(
        url,
        auth=(JIRA_EMAIL, JIRA_TOKEN),
        headers={
            "Accept": "application/json"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"Unable to retrieve ticket. Status Code: {response.status_code}"
        )

    data = response.json()

    fields = data["fields"]

    summary = fields.get("summary", "")

    # Description
    description = ""

    adf = fields.get("description")

    if adf:
        description = extract_text_from_adf(adf)

    # Comments
    comments = []

    comment_data = fields.get("comment", {})

    for comment in comment_data.get("comments", []):

        comment_text = extract_text_from_adf(
            comment.get("body", {})
        )

        if comment_text.strip():
            comments.append(comment_text)

    # Linked Tickets
    linked_tickets = []

    for link in fields.get("issuelinks", []):

        if "inwardIssue" in link:

            linked_tickets.append({
                "key": link["inwardIssue"]["key"],
                "summary": link["inwardIssue"]["fields"]["summary"]
            })

        elif "outwardIssue" in link:

            linked_tickets.append({
                "key": link["outwardIssue"]["key"],
                "summary": link["outwardIssue"]["fields"]["summary"]
            })

    # Attachments
    attachments = []

    for attachment in fields.get("attachment", []):

        attachments.append(
            attachment.get("filename")
        )

    return {
        "summary": summary,
        "description": description,
        "comments": comments,
        "linked_tickets": linked_tickets,
        "attachments": attachments
    }