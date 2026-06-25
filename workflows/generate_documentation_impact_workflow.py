from agents.candidate_article_content_fetcher import (
    fetch_candidate_content
)

from agents.help_site_impact_agent import (
    analyze_help_site_impact
)


def generate_documentation_impact(
    screenshot_file,
    selected_articles
):
    """
    Generate documentation impact
    for each selected article separately.
    """

    content_articles = fetch_candidate_content(
        selected_articles,
        max_articles=len(selected_articles)
    )

    results = []

    for article in content_articles:

        impact = analyze_help_site_impact(
            screenshot_file,
            [article]
        )

        results.append(
            {
                "title": article["title"],
                "url": article["url"],
                "impact": impact
            }
        )

    return results