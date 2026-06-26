import json
import os
import shutil

from repositories.repository_registry import (
    load_registry,
    save_registry
)


def delete_repository(
    repository
):

    if os.path.exists(
        repository["folder"]
    ):

        shutil.rmtree(
            repository["folder"]
        )

    registry = load_registry()

    registry = [

        repo

        for repo in registry

        if repo[
            "repository_id"
        ] != repository[
            "repository_id"
        ]

    ]

    save_registry(
        registry
    )