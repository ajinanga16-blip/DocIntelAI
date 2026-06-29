from documentation_intelligence.documentation_intelligence_engine import (
    discover_candidate_articles
)
from repositories.repository_loader import (
    load_repository_inventory
)

from candidate_selection.ai_candidate_selector import (
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

    inventory = load_repository_inventory(
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
    ranked = discover_candidate_articles(
        screenshot_context,
        inventory
    )

    return {
        "inventory": inventory,
        "matched_articles": ranked[:10]
    }