from agents.jira_agent import (
    fetch_jira_ticket
)

from agents.jira_intelligence_agent import (
    build_structured_requirements
)

ticket = fetch_jira_ticket("SCRUM-5")

requirements = build_structured_requirements(
    ticket
)

print(requirements)