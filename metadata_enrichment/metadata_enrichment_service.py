from urllib.parse import urlparse

from agents.article_metadata_extractor import (
    extract_article_metadata
)


def enrich_article(
    article,
    repository_name
):
    """
    Enrich repository article.

    Article content is NOT stored.
    Only searchable metadata is saved.
    """

    enriched_article = article.copy()

    enriched_article["repository"] = repository_name

    content = article.get(
        "content",
        ""
    )

    word_count = len(
        content.split()
    )

    enriched_article["word_count"] = word_count

    enriched_article["reading_time_minutes"] = max(
        1,
        round(word_count / 200)
    )

    enriched_article["domain"] = urlparse(
        article["url"]
    ).netloc

    #
    # AI Metadata
    #

    metadata = extract_article_metadata(

        title=article.get(
            "title",
            ""
        ),

        url=article.get(
            "url",
            ""
        ),

        content=content

    )

    enriched_article["description"] = metadata.get(
        "description",
        ""
    )

    enriched_article["category"] = metadata.get(
        "category",
        ""
    )

    enriched_article["features"] = metadata.get(
        "features",
        []
    )

    enriched_article["tasks"] = metadata.get(
        "tasks",
        []
    )

    enriched_article["keywords"] = metadata.get(
        "keywords",
        []
    )

    enriched_article["ui_elements"] = metadata.get(
        "ui_elements",
        []
    )

    enriched_article["error_topics"] = metadata.get(
        "error_topics",
        []
    )

    #
    # Remove article content
    #

    enriched_article.pop(
        "content",
        None
    )

    return enriched_article