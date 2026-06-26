from documentation_discovery.inventory_builder_v2 import (
    build_inventory_v2
)

from repositories.repository_manager import (
    create_repository
)

from repositories.repository_registry import (
    update_repository_status
)

from agents.article_inventory_agent import (
    save_inventory
)


def build_inventory_workflow_v2(
    repository_name,
    documentation_url
):

    repository_folder = create_repository(
        repository_name,
        documentation_url
    )

    inventory = build_inventory_v2(
        documentation_url
    )

    save_inventory(
        repository_folder,
        inventory
    )

    update_repository_status(
        repository_name,
        "Ready",
        len(inventory)
    )

    return inventory