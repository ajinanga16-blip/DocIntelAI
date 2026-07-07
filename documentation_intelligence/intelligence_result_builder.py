def build_intelligence_result(
    work_item,
    analyzed_articles
):
    """
    Builds a simplified Documentation
    Intelligence result that can be
    rendered by any UI.

    Current modules:

    - Gap Analysis
    - Impact Analysis
    - Screenshot Intelligence
    """

    if not analyzed_articles:

        return {

            "work_item": work_item,

            "status": "Create New Article",

            "coverage": 0,

            "best_match": None,

            "alternative_matches": [],

            "missing_topics": [],

            "recommended_action":
                "Create new documentation.",

            "generated_content": ""

        }

    #
    # Best article
    #

    best = analyzed_articles[0]

    #
    # Alternatives
    #

    alternatives = analyzed_articles[1:3]

    return {

        "work_item": work_item,

        "status":
            "Update Existing Article",

        "coverage":
            best["analysis"].get(
                "coverage_score",
                ""
            ),

        "best_match": {

            "title":
                best.get(
                    "title",
                    ""
                ),

            "url":
                best.get(
                    "url",
                    ""
                )

        },

        "alternative_matches":
            alternatives,

        "missing_topics": [

            best["analysis"].get(
                "gap",
                ""
            )

        ],

        "recommended_action":

            best["analysis"].get(
                "recommended_change",
                ""
            ),

        "generated_content":

            best["analysis"].get(
                "generated_content",
                ""
            )

    }