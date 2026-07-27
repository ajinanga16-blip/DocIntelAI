def action_plan_to_requirements(action_plan):
    """
    Converts a Documentation Action Plan into the
    structured requirements format expected by the
    documentation generation engine.
    """

    work_item = action_plan.get("work_item", {})

    impacted_articles = action_plan.get(
        "impacted_articles",
        []
    )

    documentation_notes = []

    for article in impacted_articles:

        title = article.get("title", "")

        required_change = article.get(
            "required_change",
            ""
        )

        gap = article.get(
            "gap",
            ""
        )

        documentation_notes.append(
            f"{title}: {required_change}"
        )

        if gap:

            documentation_notes.append(
                f"Gap: {gap}"
            )

    return {

        "feature_name":
            work_item.get(
                "summary",
                ""
            ),

        "feature_description":
            work_item.get(
                "description",
                ""
            ),

        "acceptance_criteria":
            work_item.get(
                "acceptance_criteria",
                []
            ),

        "documentation_notes":
            documentation_notes,

        "implementation_notes": [

            f"Overall Action: {action_plan.get('overall_action','')}",

            f"Estimated Effort: {action_plan.get('estimated_effort','')}"

        ],

        "dependencies": [],

        "attachments": []

    }