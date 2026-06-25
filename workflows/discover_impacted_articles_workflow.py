from agents.help_site_discovery_workflow import (
    discover_help_site_articles
)

from agents.help_site_query_builder import (
    build_help_site_queries
)

from agents.intelligent_article_matcher import (
    intelligent_match_articles
)


def discover_impacted_articles(
    help_site_url,
    screenshot_change
):
    """
    Step 1:
    Discover impacted documentation articles.
    """

    inventory = discover_help_site_articles(
        help_site_url
    )

    queries = build_help_site_queries(
        screenshot_change
    )

    results = intelligent_match_articles(
        queries,
        inventory
    )

    return results