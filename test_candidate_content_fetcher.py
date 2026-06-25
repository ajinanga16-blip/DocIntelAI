from agents.candidate_article_content_fetcher import (
    fetch_candidate_content
)

matched_articles = [
    {
        "title":
            "Setting up Roles & Role-Based Access Controls",

        "url":
            "https://support.freshservice.com/support/solutions/articles/50000002933-setting-up-roles-role-based-access-controls",

        "confidence":
            90,

        "reason":
            "Role-related functionality"
    }
]

results = fetch_candidate_content(
    matched_articles
)

print(
    f"Articles Fetched: {len(results)}"
)

if results:

    print(
        results[0]["title"]
    )

    print(
        len(
            results[0]["content"]
        )
    )