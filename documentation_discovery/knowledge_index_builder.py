from documentation_discovery.article_metadata_enricher import (
    enrich_article
)


def build_knowledge_index(
    inventory,
    progress_callback=None
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

        #
        # Report Progress
        #

        if progress_callback:

            progress_callback(

                index + 1,

                total,

                article.get(
                    "title",
                    ""
                )

            )

        enriched_inventory.append(

            enrich_article(
                article
            )

        )

    return enriched_inventory