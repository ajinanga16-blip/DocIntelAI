from documentation_discovery.inventory_builder import (
    build_inventory
)


def build_inventory_v2(
    documentation_url
):
    """
    Temporary wrapper to maintain
    backward compatibility.
    """

    return build_inventory(
        documentation_url
    )