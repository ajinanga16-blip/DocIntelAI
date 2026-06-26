import json
import os
import uuid
from datetime import datetime

REGISTRY_FILE = "data/repositories/repositories.json"

#
# Development only.
# Later this will come
# from the logged-in user.
#
ORGANIZATION_ID = "local-dev"


def load_registry():

    if not os.path.exists(
        REGISTRY_FILE
    ):
        return []

    with open(
        REGISTRY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_registry(
    registry
):

    os.makedirs(
        "data/repositories",
        exist_ok=True
    )

    with open(
        REGISTRY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            registry,
            file,
            indent=4,
            ensure_ascii=False
        )


def register_repository(
    repository_name,
    base_url,
    folder
):

    registry = load_registry()

    registry.append({

        "organization_id": ORGANIZATION_ID,

        "repository_id": str(
            uuid.uuid4()
        ),

        "repository_name": repository_name,

        "base_url": base_url,

        "folder": folder,

        "status": "Building",

        "article_count": 0,

        "last_updated": ""

    })

    save_registry(
        registry
    )


def update_repository_status(
    repository_name,
    status,
    article_count
):

    registry = load_registry()

    for repo in registry:

        if repo[
            "repository_name"
        ] == repository_name:

            repo[
                "status"
            ] = status

            repo[
                "article_count"
            ] = article_count

            repo[
                "last_updated"
            ] = datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )

    save_registry(
        registry
    )


def get_repositories():

    registry = load_registry()

    return [

        repo

        for repo in registry

        if repo[
            "organization_id"
        ] == ORGANIZATION_ID

    ]