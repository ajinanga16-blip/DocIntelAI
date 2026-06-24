def build_review_package(
    clusters,
    impacts
):

    package = []

    for cluster, impact in zip(
        clusters,
        impacts
    ):

        package.append(
            {
                "cluster": cluster,
                "impact": impact
            }
        )

    return package