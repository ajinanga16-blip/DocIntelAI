def build_help_site_queries(
    change_data
):

    queries = []

    for item in change_data.get(
        "removed_elements",
        []
    ):

        queries.append(item)

    for item in change_data.get(
        "added_elements",
        []
    ):

        queries.append(item)

    for nav in change_data.get(
        "navigation_changes",
        []
    ):

        queries.append(
            nav["old_path"]
        )

        queries.append(
            nav["new_path"]
        )

    return list(
        set(queries)
    )