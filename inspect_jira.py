import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

ticket_id = "SCRUM-5"

url = f"{os.getenv('JIRA_URL')}/rest/api/3/issue/{ticket_id}"

response = requests.get(
    url,
    auth=(
        os.getenv("JIRA_EMAIL"),
        os.getenv("JIRA_TOKEN")
    ),
    headers={"Accept": "application/json"}
)

data = response.json()

print(json.dumps(data["fields"], indent=2))