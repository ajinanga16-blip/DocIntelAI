from agents.article_clustering_agent import (
    cluster_articles
)

from agents.article_impact_agent import (
    analyze_cluster_impact
)

from agents.review_package_agent import (
    build_review_package
)

from agents.impact_map_agent import (
    build_impact_map
)


def run_screenshot_impact_workflow(
    screenshot_change,
    articles
):

    clusters = cluster_articles(
        articles
    )

    impacts = []

    # Placeholder for now

    review_package = build_review_package(
        [],
        []
    )

    impact_map = build_impact_map(
        review_package
    )

    return {
        "clusters": clusters,
        "review_package":
            review_package,
        "impact_map":
            impact_map
    }