def filter_article_links(
    links
):

    filtered_links = []

    exclude_keywords = [
        "login",
        "community",
        "academy",
        "pricing",
        "careers",
        "contact",
        "product",
        "support/home",
        "support home",
        "terms",
        "privacy",
        "blog",
        "video",
        "training"
    ]

    for item in links:

        title = (
            item.get(
                "title",
                ""
            )
            .lower()
        )

        url = (
            item.get(
                "url",
                ""
            )
            .lower()
        )

        skip = False

        for keyword in exclude_keywords:

            if (
                keyword in title
                or
                keyword in url
            ):

                skip = True

                break

        if not skip:

            filtered_links.append(
                item
            )

    return filtered_links