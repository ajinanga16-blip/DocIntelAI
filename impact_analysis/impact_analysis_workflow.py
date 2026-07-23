from documentation_intelligence.documentation_intelligence_engine import (
    discover_candidate_articles
)

from impact_analysis.impact_analysis_prompts import (
    analyze_article
)

from documentation_actions.action_planner import (
    build_action_plan
)


def analyze_impact_work_item(
    repository_name,
    work_item
):
    """
    Analyze one work item and return
    a Documentation Action Plan.
    """

    articles = discover_candidate_articles(

        repository_name,

        work_item

    )

    analyzed_articles = []

    #
    # Analyze Top 3 articles
    #

    for article in articles[:3]:

        analysis = analyze_article(

            work_item,

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

    action_plan = build_action_plan(

        work_item,

        analyzed_articles

    )

    return action_plan