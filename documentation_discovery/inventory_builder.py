from documentation_discovery.discovery_manager import (
    discover_site
)

from documentation_discovery.sitemap_parser import (
    parse_sitemap
)

from inventory.inventory_crawler_v2 import (
    crawl_help_site_v2
)

from inventory.inventory_validator import (
    validate_inventory
)


def build_inventory(
    documentation_url
):
    """
    Universal Documentation Discovery Engine.

    Decides the best strategy for
    discovering documentation.
    """

    strategy = discover_site(
        documentation_url
    )

    #
    # Sitemap
    #

    if strategy["strategy"] == "sitemap":

        inventory = parse_sitemap(
            strategy["sitemap"]
        )

    #
    # Crawl
    #

    else:

        inventory = crawl_help_site_v2(
            documentation_url
        )

    #
    # Validate
    #

    inventory = validate_inventory(
        inventory
    )

    from documentation_discovery.knowledge_index_builder import (
        build_knowledge_index
    )

    inventory = build_knowledge_index(
        inventory
    )

    return inventory