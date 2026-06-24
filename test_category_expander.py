from agents.category_expander_agent import (
    expand_category
)

results = expand_category(
    "https://support.freshservice.com/support/solutions/50000000126"
)

print(
    f"Links Found: {len(results)}"
)

for item in results[:20]:

    print(
        item["title"]
    )

    print(
        item["url"]
    )

    print("---")