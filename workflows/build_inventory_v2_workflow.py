from inventory.inventory_builder_v2 import (
    build_inventory_v2
)

from agents.article_inventory_agent import (
    save_inventory
)


def build_inventory_workflow_v2(
    help_site_url
):
    """
    Builds a fresh documentation
    inventory using Crawler V2.
    """

    inventory = build_inventory_v2(
        help_site_url
    )

    save_inventory(
        inventory
    )

    return inventory