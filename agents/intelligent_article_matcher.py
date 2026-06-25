from ranking.hybrid_ranker import (
    rank_articles
)


def intelligent_match_articles(
    queries,
    article_inventory,
    max_results=10
):
    """
    Hybrid article matcher.

    Uses:
    - Title matching
    - Content matching
    - Keyword matching
    - Synonym expansion

    Returns the highest ranked articles.
    """

    ranked_articles = rank_articles(
        queries,
        article_inventory
    )

    return {
        "matched_articles": ranked_articles[
            :max_results
        ]
    }