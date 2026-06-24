from agents.article_content_matcher_agent import (
    match_article_content
)

queries = [
    "Navigation Role dropdown",
    "Assign User Role"
]

articles = [
    {
        "title":
            "Creating a new custom role",
        "url":
            "url1",
        "content":
            "Assign User Role allows administrators to assign navigation roles."
    },
    {
        "title":
            "Alert Management",
        "url":
            "url2",
        "content":
            "Configure alerts and monitoring integrations."
    }
]

result = match_article_content(
    queries,
    articles
)

print(result)