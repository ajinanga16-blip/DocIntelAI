from agents.article_matcher_agent import (
    match_articles
)

from agents.candidate_article_content_fetcher import (
    fetch_candidate_content
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

title_matches = match_articles(
    queries,
    inventory
)

matched_articles = (
    title_matches.get(
        "matched_articles",
        []
    )
)

print("\nMATCHED ARTICLES\n")

print(
    len(
        matched_articles
    )
)

content_articles = (
    fetch_candidate_content(
        matched_articles
    )
)

print("\nCONTENT ARTICLES\n")

print(
    len(
        content_articles
    )
)

if content_articles:

    print(
        content_articles[0]["title"]
    )

    print(
        len(
            content_articles[0]["content"]
        )
    )