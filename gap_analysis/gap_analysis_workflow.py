from documentation_intelligence.documentation_intelligence_engine import (
    discover_candidate_articles
)

from gap_analysis.gap_analysis_prompts import (
    analyze_article
)

from documentation_actions.action_planner import (
    build_action_plan
)


def analyze_gap_tickets(
    repository_name,
    tickets
):
    """
    Analyze each work item and return a
    Documentation Action Plan.
    """

    results = []

    for ticket in tickets:

        #
        # Discover candidate articles
        #

        articles = discover_candidate_articles(

            repository_name,

            ticket

        )

        #
        # Analyze Top 3 only
        #

        analyzed_articles = []

        for article in articles[:3]:

            analysis = analyze_article(

                ticket,

                article

            )

            analyzed_articles.append({

                "title": article.get(
                    "title",
                    ""
                ),

                "url": article.get(
                    "url",
                    ""
                ),

                "confidence": article.get(
                    "confidence",
                    0
                ),

                "analysis": analysis

            })

        #
        # Build Documentation Action Plan
        #

        action_plan = build_action_plan(

            ticket,

            analyzed_articles

        )

        results.append(
            action_plan
        )

    return results