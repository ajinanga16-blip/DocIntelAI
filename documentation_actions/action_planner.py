def build_action_plan(
    work_item,
    analyzed_articles
):
    """
    Builds a Documentation Action Plan.

    One work item can impact multiple
    documentation articles.
    """

    action_plan = {

        "work_item": work_item,

        "overall_action": "",

        "estimated_effort": "",

        "impacted_articles": []

    }

    if not analyzed_articles:

        action_plan["overall_action"] = "Create New Article"

        action_plan["estimated_effort"] = "High"

        return action_plan

    for article in analyzed_articles:

        analysis = article.get(
            "analysis",
            {}
        )

        action_plan["impacted_articles"].append({

            "title": article.get(
                "title",
                ""
            ),

            "url": article.get(
                "url",
                ""
            ),

            "coverage": analysis.get(
                "coverage_score",
                ""
            ),

            "required_change": analysis.get(
                "recommended_change",
                ""
            ),

            "gap": analysis.get(
                "gap",
                ""
            ),

            "generate": False

        })

    count = len(
        action_plan["impacted_articles"]
    )

    if count == 1:

        action_plan["overall_action"] = (
            "Update Existing Article"
        )

        action_plan["estimated_effort"] = "Low"

    elif count <= 3:

        action_plan["overall_action"] = (
            "Update Existing Documentation"
        )

        action_plan["estimated_effort"] = "Medium"

    else:

        action_plan["overall_action"] = (
            "Documentation Review Required"
        )

        action_plan["estimated_effort"] = "High"

    return action_plan