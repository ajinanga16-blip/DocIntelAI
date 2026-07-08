from agents.category_expander_agent import (
    expand_category
)

from agents.article_link_filter_agent import (
    filter_article_links
)

links = expand_category(
    "https://support.freshservice.com/support/solutions/50000000126"
)

filtered = filter_article_links(
    links
)

print(
    f"Original Links: {len(links)}"
)

print(
    f"Filtered Links: {len(filtered)}"
)

for item in filtered[:20]:

    print(
        item["title"]
    )

    print(
        item["url"]
    )

    print("---")