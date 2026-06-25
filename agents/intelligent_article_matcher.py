from agents.article_matcher_agent import (
    match_articles
)

from agents.candidate_article_content_fetcher import (
    fetch_candidate_content
)

from agents.article_content_matcher_agent import (
    match_article_content
)


def intelligent_match_articles(
    queries,
    article_inventory
):

    #
    # Stage 1
    # Title Match
    #

    title_matches = match_articles(
        queries,
        article_inventory
    )

    matched_articles = (
        title_matches.get(
            "matched_articles",
            []
        )
    )

    if not matched_articles:

        return {
            "matched_articles": []
        }

    #
    # Stage 2
    # Fetch Content
    #

    content_articles = (
        fetch_candidate_content(
            matched_articles,
            max_articles=10
        )
    )

    #
    # Stage 3
    # Content Match
    #

    final_matches = (
        match_article_content(
            queries,
            content_articles
        )
    )

    return final_matches