from agents.article_content_fetcher import (
    fetch_article_content
)

result = fetch_article_content(
    "https://support.freshservice.com/support/solutions/50000000126"
)

print(
    result["title"]
)

print(
    result["content"][:500]
)