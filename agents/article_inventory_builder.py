from agents.article_content_fetcher import (
    fetch_article_content
)

from agents.article_metadata_extractor import (
    extract_article_metadata
)


def build_article_inventory(
    articles
):

    inventory = []

    for article in articles:

        content = fetch_article_content(
            article["url"]
        )

        if not content:
            continue

        metadata = extract_article_metadata(

            title=content.get(
                "title",
                article.get("title", "")
            ),

            url=content.get(
                "url",
                article["url"]
            ),

            content=content.get(
                "content",
                ""
            )

        )

        inventory.append({

            "title": content.get(
                "title",
                article.get("title", "")
            ),

            "url": content.get(
                "url",
                article["url"]
            ),

            "description": metadata.get(
                "description",
                ""
            ),

            "category": metadata.get(
                "category",
                ""
            ),

            "features": metadata.get(
                "features",
                []
            ),

            "tasks": metadata.get(
                "tasks",
                []
            ),

            "ui_elements": metadata.get(
                "ui_elements",
                []
            ),

            "error_topics": metadata.get(
                "error_topics",
                []
            ),

            "keywords": metadata.get(
                "keywords",
                []
            )

        })

    return inventory