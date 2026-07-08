from agents.intelligent_article_matcher import (
    intelligent_match_articles
)

from agents.article_inventory_agent import (
    load_inventory
)

queries = [
    "Alert Management",
    "Alerts",
    "Monitoring Tools"
]

inventory = load_inventory()

from agents.article_matcher_agent import (
    match_articles
)

title_matches = match_articles(
    queries,
    inventory
)

print("TITLE MATCHES")
print(title_matches)