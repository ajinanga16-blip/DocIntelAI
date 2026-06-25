from documentation_discovery.article_metadata_enricher import (
    enrich_article
)


def build_knowledge_index(
    inventory
):
    """
    Enriches the inventory with
    lightweight metadata.
    """

    enriched = []

    total = len(inventory)

    for index, article in enumerate(inventory):

        print(
            f"Enriching {index + 1}/{total}"
        )

        enriched.append(
            enrich_article(
                article
            )
        )

    return enriched