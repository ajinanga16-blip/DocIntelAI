def validate_inventory(
    inventory
):
    """
    Removes duplicates and invalid entries.
    """

    seen = set()

    validated = []

    for article in inventory:

        url = article.get(
            "url",
            ""
        ).strip()

        title = article.get(
            "title",
            ""
        ).strip()

        if not url or not title:
            continue

        if url in seen:
            continue

        seen.add(url)

        validated.append(article)

    return validated