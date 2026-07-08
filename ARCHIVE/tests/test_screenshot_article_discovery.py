from agents.screenshot_article_discovery_workflow import (
    discover_impacted_articles
)

change_data = {
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

articles = [
    {
        "title":
            "Assign User Role",
        "url":
            "url1"
    },
    {
        "title":
            "Create User",
        "url":
            "url2"
    }
]

result = discover_impacted_articles(
    change_data,
    articles
)

print(result)