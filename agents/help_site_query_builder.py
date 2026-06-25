def build_help_site_queries(change_data):

    queries = []

    #
    # New Screenshot Discovery Model
    #

    queries.extend(
        change_data.get(
            "keywords",
            []
        )
    )

    queries.extend(
        change_data.get(
            "ui_elements",
            []
        )
    )

    queries.extend(
        change_data.get(
            "buttons",
            []
        )
    )

    queries.extend(
        change_data.get(
            "labels",
            []
        )
    )

    queries.extend(
        change_data.get(
            "menus",
            []
        )
    )

    if change_data.get(
        "page_title"
    ):

        queries.append(
            change_data[
                "page_title"
            ]
        )

    if change_data.get(
        "screen_name"
    ):

        queries.append(
            change_data[
                "screen_name"
            ]
        )

    queries.extend(
        change_data.get(
            "breadcrumbs",
            []
        )
    )

    #
    # Backward Compatibility
    #

    queries.extend(
        change_data.get(
            "added_elements",
            []
        )
    )

    queries.extend(
        change_data.get(
            "removed_elements",
            []
        )
    )

    for nav in change_data.get(
        "navigation_changes",
        []
    ):

        queries.append(
            nav.get(
                "old_path",
                ""
            )
        )

        queries.append(
            nav.get(
                "new_path",
                ""
            )
        )

    #
    # Cleanup
    #

    queries = [
        q.strip()
        for q in queries
        if q and q.strip()
    ]

    return list(
        set(queries)
    )