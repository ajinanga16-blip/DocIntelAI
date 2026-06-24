from agents.article_inventory_builder import (
    build_article_inventory
)

articles = [
    {
        "title":
            "Alert Management in Freshservice - An Overview",
        "url":
            "https://support.freshservice.com/support/solutions/articles/50000002885-alert-management-in-freshservice-an-overview"
    }
]

inventory = build_article_inventory(
    articles
)

print(
    inventory[0].keys()
)

print(
    inventory[0]["title"]
)

print(
    len(
        inventory[0]["content"]
    )
)