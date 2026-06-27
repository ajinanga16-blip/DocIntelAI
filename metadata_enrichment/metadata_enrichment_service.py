from urllib.parse import urlparse


def enrich_article(article, repository_name):
    """
    Add metadata to a discovered article.
    """

    enriched_article = article.copy()

    enriched_article["repository"] = repository_name

    enriched_article["word_count"] = 0

    enriched_article["reading_time_minutes"] = 0

    enriched_article["domain"] = urlparse(
        article["url"]
    ).netloc

    return enriched_article