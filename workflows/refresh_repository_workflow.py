import os

from workflows.build_inventory_v2_workflow import (
    build_inventory_workflow_v2
)


def refresh_repository(
    repository
):
    """
    Refreshes a repository by
    rebuilding its inventory.
    """

    inventory_file = os.path.join(
        repository["folder"],
        "inventory.json"
    )

    if os.path.exists(
        inventory_file
    ):

        os.remove(
            inventory_file
        )

    return build_inventory_workflow_v2(

        repository["repository_name"],

        repository["base_url"]

    )