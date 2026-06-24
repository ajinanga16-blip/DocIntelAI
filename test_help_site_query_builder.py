from agents.help_site_query_builder import (
    build_help_site_queries
)

sample = {
    "removed_elements": [
        "Navigation Role dropdown"
    ],

    "added_elements": [
        "User Role page"
    ],

    "navigation_changes": [
        {
            "old_path":
                "Create User > Assign User Role",

            "new_path":
                "User Role > Assign User Role"
        }
    ]
}

print(
    build_help_site_queries(
        sample
    )
)