from agents.help_site_query_builder import (
    build_help_site_queries
)

from agents.article_matcher_agent import (
    match_articles
)


def discover_impacted_articles(
    change_data,
    articles
):

    queries = build_help_site_queries(
        change_data
    )

    matches = match_articles(
        queries,
        articles
    )

    return matches