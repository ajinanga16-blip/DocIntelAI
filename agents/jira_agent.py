import os
import requests
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")


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

    summary = data["fields"]["summary"]

    description = ""

    adf = data["fields"].get("description")

    if adf and "content" in adf:

        for block in adf["content"]:

            if "content" in block:

                for item in block["content"]:

                    if item.get("type") == "text":

                        description += item.get("text", "") + "\n"

    return {
        "summary": summary,
        "description": description
    }