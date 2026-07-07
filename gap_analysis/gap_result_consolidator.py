def consolidate_gap_result(
    work_item,
    analyzed_articles
):
    """
    Consolidates multiple article analyses
    into one actionable recommendation.
    """

    if not analyzed_articles:

        return {

            "work_item": work_item,

            "status": "Create New Article",

            "best_article": None,

            "coverage": 0,

            "missing_topics": [],

            "recommendation":
                "No relevant documentation was found.",

            "generated_content": "",

            "alternatives": []

        }

    #
    # Highest confidence article
    #

    best = max(

        analyzed_articles,

        key=lambda article:
            article.get(
                "confidence",
                0
            )

    )

    #
    # Alternatives
    #

    alternatives = sorted(

        analyzed_articles,

        key=lambda article:
            article.get(
                "confidence",
                0
            ),

        reverse=True

    )[1:3]

    analysis = best["analysis"]

    return {

        "work_item": work_item,

        "status":
            "Update Existing Article",

        "best_article": {

            "title":
                best["title"],

            "url":
                best["url"]

        },

        "coverage":

            analysis.get(
                "coverage_score",
                ""
            ),

        "missing_topics": [

            analysis.get(
                "gap",
                ""
            )

        ],

        "recommendation":

            analysis.get(
                "recommended_change",
                ""
            ),

        "generated_content":

            analysis.get(
                "generated_content",
                ""
            ),

        "alternatives": [

            {

                "title":
                    article["title"],

                "confidence":
                    article.get(
                        "confidence",
                        0
                    )

            }

            for article in alternatives

        ]

    }