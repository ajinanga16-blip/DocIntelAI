from agents.help_site_discovery_workflow import (
    discover_help_site_articles
)

from agents.screenshot_article_discovery_workflow import (
    discover_impacted_articles
)

articles = discover_help_site_articles(
    "https://support.freshservice.com"
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

result = discover_impacted_articles(
    change_data,
    articles
)

print(result)