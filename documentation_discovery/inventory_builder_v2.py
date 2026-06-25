from inventory.inventory_crawler_v2 import (
    crawl_help_site_v2
)

from inventory.inventory_validator import (
    validate_inventory
)


def build_inventory_v2(
    help_site_url
):
    """
    Inventory Builder V2

    Crawls the complete documentation
    site and validates the inventory.
    """

    inventory = crawl_help_site_v2(
        help_site_url
    )

    inventory = validate_inventory(
        inventory
    )

    return inventory