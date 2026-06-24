def build_impact_map(
    review_package
):

    impact_map = []

    for item in review_package:

        impact_map.append(
            {
                "cluster":
                    item["cluster"],
                "article_count":
                    len(
                        item["cluster"]
                        .get(
                            "articles",
                            []
                        )
                    ),
                "impact":
                    item["impact"]
            }
        )

    return impact_map