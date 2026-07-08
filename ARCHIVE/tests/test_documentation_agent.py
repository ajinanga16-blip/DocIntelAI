from agents.jira_agent import fetch_jira_ticket

from agents.jira_intelligence_agent import (
    build_structured_requirements
)

from agents.documentation_agent import (
    generate_documentation_from_requirements
)


ticket = fetch_jira_ticket(
    "SCRUM-5"
)

requirements = build_structured_requirements(
    ticket
)

result = generate_documentation_from_requirements(
    requirements,
    "User Guide"
)

print(result)