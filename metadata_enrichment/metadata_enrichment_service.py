from urllib.parse import urlparse


def enrich_article(article, repository_name):
    """
    Add metadata to a discovered article.
    """

    enriched_article = article.copy()

    enriched_article["repository"] = repository_name

    content = article.get("content", "")

    word_count = len(content.split())

    enriched_article["word_count"] = word_count

    enriched_article["reading_time_minutes"] = max(
        1,
        round(word_count / 200)
    )

    enriched_article["domain"] = urlparse(
        article["url"]
    ).netloc

    return enriched_article