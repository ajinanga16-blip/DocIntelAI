def filter_real_articles(
    links
):

    results = []

    for item in links:

        url = item.get(
            "url",
            ""
        ).lower()

        title = item.get(
            "title",
            ""
        ).lower()

        if (
            "/articles/"
            in url
        ):

            results.append(
                item
            )

    return results