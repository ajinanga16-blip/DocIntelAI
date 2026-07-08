from agents.article_matcher_agent import (
    match_articles
)

queries = [
    "User Role page",
    "Assign User Role",
    "Navigation Role dropdown"
]

articles = [
    {
        "title":
        "Assign User Role",
        "url":
        "url1"
    },
    {
        "title":
        "Create User",
        "url":
        "url2"
    },
    {
        "title":
        "Alert Management",
        "url":
        "url3"
    }
]

result = match_articles(
    queries,
    articles
)

print(result)