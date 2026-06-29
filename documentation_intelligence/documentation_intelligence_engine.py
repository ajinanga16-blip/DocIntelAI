from candidate_selection.ai_candidate_selector import (
    ai_candidate_search
)

from agents.candidate_article_content_fetcher import (
    fetch_candidate_content
)

from ranking.hybrid_ranker import (
    rank_articles
)


def discover_candidate_articles(
    context,
    inventory
):
    """
    Shared Documentation Intelligence Engine.

    Returns the best candidate articles
    for any Documentation Intelligence module.
    """

    candidates = ai_candidate_search(
        context,
        inventory
    )

    content_articles = fetch_candidate_content(
        candidates["matched_articles"],
        max_articles=len(
            candidates["matched_articles"]
        )
    )

    queries = []

    queries.extend(
        context.get(
            "keywords",
            []
        )
    )

    queries.extend(
        context.get(
            "ui_elements",
            []
        )
    )

    if context.get(
        "page_title"
    ):

        queries.append(
            context["page_title"]
        )

    ranked = rank_articles(
        queries,
        content_articles
    )

    return ranked