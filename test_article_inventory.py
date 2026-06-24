from agents.article_inventory_agent import (
    save_inventory,
    load_inventory,
    inventory_exists
)

sample_articles = [
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

save_inventory(
    sample_articles
)

print(
    inventory_exists()
)

print(
    load_inventory()
)