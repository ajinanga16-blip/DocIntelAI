from documentation_discovery.discovery_manager import (
    discover_site
)

from documentation_discovery.sitemap_parser import (
    parse_sitemap
)

from documentation_discovery.navigation_crawler import (
    crawl_documentation
)

from documentation_discovery.inventory_validator import (
    validate_inventory
)

from documentation_discovery.knowledge_index_builder import (
    build_knowledge_index
)


def build_inventory(
    documentation_url
):
    """
    Universal Documentation Discovery Engine.

    Automatically determines the best
    strategy to discover documentation.
    """

    strategy = discover_site(
        documentation_url
    )

    #
    # Discovery
    #

    if strategy["strategy"] == "sitemap":

        print(
            "Using Sitemap Discovery..."
        )

        inventory = parse_sitemap(
            strategy["sitemap"]
        )

        #
        # Mark discovery source
        #

        for article in inventory:

            article[
                "discovered_by"
            ] = "sitemap"

    else:

        print(
            "Using Navigation Crawl..."
        )

        inventory = crawl_documentation(
            documentation_url
        )

    #
    # Validation
    #

    inventory = validate_inventory(
        inventory
    )

    #
    # Lightweight enrichment
    #

    inventory = build_knowledge_index(
        inventory
    )

    print(
        f"Inventory Size: {len(inventory)}"
    )

    return inventory