import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

REPOSITORIES_FOLDER = PROJECT_ROOT / "data" / "repositories"


def load_repository_inventory(repository_name):
    """
    Load the inventory for a repository.
    """

    inventory_file = (
        REPOSITORIES_FOLDER
        / repository_name
        / "inventory.json"
    )

    if not inventory_file.exists():
        return []

    with open(
        inventory_file,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)