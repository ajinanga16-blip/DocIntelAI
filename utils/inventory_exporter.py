import json
import os

import pandas as pd


def export_inventory(
    repository_folder
):

    inventory_file = os.path.join(
        repository_folder,
        "inventory.json"
    )

    with open(
        inventory_file,
        "r",
        encoding="utf-8"
    ) as file:

        inventory = json.load(
            file
        )

    df = pd.DataFrame(
        inventory
    )

    export_path = os.path.join(
        repository_folder,
        "inventory.xlsx"
    )

    df.to_excel(
        export_path,
        index=False
    )

    return export_path