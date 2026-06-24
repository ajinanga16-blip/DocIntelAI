import json
import os


INVENTORY_FILE = (
    "data/article_inventory.json"
)


def save_inventory(
    articles
):

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(
        INVENTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            articles,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_inventory():

    if not os.path.exists(
        INVENTORY_FILE
    ):

        return []

    with open(
        INVENTORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def inventory_exists():

    return os.path.exists(
        INVENTORY_FILE
    )