from agents.help_site_discovery_workflow import (
    discover_help_site_articles
)

from search_engines.ai_candidate_search_engine import (
    ai_candidate_search
)

from agents.candidate_article_content_fetcher import (
    fetch_candidate_content
)

from ranking.hybrid_ranker import (
    rank_articles
)


def discover_impacted_articles_v2(
    help_site_url,
    screenshot_context
):
    """
    V2 Discovery Workflow

    Screenshot
        ↓
    Inventory
        ↓
    AI Candidate Selection
        ↓
    Fetch Candidate Content
        ↓
    Hybrid Ranking
    """

    #
    # Step 1
    #

    inventory = discover_help_site_articles(
        help_site_url
    )

    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active

    ws.append(["Title", "URL"])

    for article in inventory:

        ws.append([
            article.get("title", ""),
            article.get("url", "")
        ])

    wb.save("inventory.xlsx")


    print(f"Inventory Size: {len(inventory)}")

    for article in inventory:

        title = article.get("title", "").lower()

        if (
        "single sign-on" in title
        or "where do i configure" in title
        or "50000000143" in article.get("url", "")
        ):

            print("FOUND IN INVENTORY")
            print(article["title"])
            print(article["url"])

    #
    # Step 2
    #

    candidates = ai_candidate_search(
        screenshot_context,
        inventory
    )

    #
    # Step 3
    #

    content_articles = fetch_candidate_content(
        candidates["matched_articles"],
        max_articles=len(
            candidates["matched_articles"]
        )
    )

    #
    # Step 4
    #

    queries = []

    queries.extend(
        screenshot_context.get(
            "keywords",
            []
        )
    )

    queries.extend(
        screenshot_context.get(
            "ui_elements",
            []
        )
    )

    if screenshot_context.get(
        "page_title"
    ):

        queries.append(
            screenshot_context[
                "page_title"
            ]
        )

    ranked = rank_articles(
        queries,
        content_articles
    )

    return {
        "inventory": inventory,
        "matched_articles": ranked[:10]
    }