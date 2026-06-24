from agents.article_content_fetcher import (
    fetch_article_content
)


def build_article_inventory(
    articles
):

    inventory = []

    for article in articles:

        content = fetch_article_content(
            article["url"]
        )

        if content:

            inventory.append(
                content
            )

    return inventory