from agents.help_site_discovery_workflow import (
    discover_help_site_articles
)

articles = discover_help_site_articles(
    "https://support.freshservice.com"
)

print(
    f"Articles Found: {len(articles)}"
)

for article in articles[:10]:

    print(
        article["title"]
    )