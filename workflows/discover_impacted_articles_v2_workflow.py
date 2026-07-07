from documentation_intelligence.documentation_intelligence_engine import (
    discover_candidate_articles
)

from repositories.repository_loader import (
    load_repository_inventory
)


def discover_impacted_articles_v2(

    repository_name,

    screenshot_context

):
    """
    Screenshot Intelligence V2
    """

    inventory = load_repository_inventory(

        repository_name

    )

    ranked = discover_candidate_articles(

        repository_name,

        screenshot_context

    )

    return {

        "inventory": inventory,

        "matched_articles": ranked[:10]

    }