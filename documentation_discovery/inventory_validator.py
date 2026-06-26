def validate_inventory(
    inventory
):
    """
    Cleans and validates a
    documentation inventory.
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

        if not url:
            continue

        if url in seen:
            continue

        seen.add(url)

        validated.append({

            "title": title,

            "url": url,

            "description": article.get(
                "description",
                ""
            ),

            "discovered_by": article.get(
                "discovered_by",
                "unknown"
            )

        })

    return validated