from agents.help_site_discovery_agent import (
    discover_candidate_articles
)

results = discover_candidate_articles(
    "https://support.freshservice.com",
    [
        "Navigation Role dropdown",
        "User Role page"
    ]
)

print(
    f"Articles Found: {len(results)}"
)

print(
    results[0]["url"]
)