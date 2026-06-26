import json
import os


def save_inventory(
    repository_folder,
    articles
):
    """
    Saves the inventory inside
    the repository folder.
    """

    inventory_file = os.path.join(
        repository_folder,
        "inventory.json"
    )

    with open(
        inventory_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            articles,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_inventory(
    repository_folder
):

    inventory_file = os.path.join(
        repository_folder,
        "inventory.json"
    )

    if not os.path.exists(
        inventory_file
    ):

        return []

    with open(
        inventory_file,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def inventory_exists(
    repository_folder
):

    inventory_file = os.path.join(
        repository_folder,
        "inventory.json"
    )

    return os.path.exists(
        inventory_file
    )