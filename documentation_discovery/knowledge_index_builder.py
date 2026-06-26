from documentation_discovery.article_metadata_enricher import (
    enrich_article
)


def build_knowledge_index(
    inventory
):
    """
    Creates a lightweight Knowledge Index
    from the discovered inventory.
    """

    enriched_inventory = []

    total = len(inventory)

    print(f"Enriching {total} articles...")

    for index, article in enumerate(inventory):

        print(
            f"[{index + 1}/{total}] "
            f"{article.get('title', article.get('url'))}"
        )

        enriched_inventory.append(
            enrich_article(
                article
            )
        )

    return enriched_inventory