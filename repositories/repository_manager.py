import os
import json
import re

from repositories.repository_registry import (
    register_repository
)


REPOSITORY_ROOT = "data/repositories"


def repository_slug(name):

    return re.sub(
        r"[^a-zA-Z0-9]+",
        "_",
        name.lower()
    ).strip("_")


def create_repository(
    repository_name,
    base_url
):

    slug = repository_slug(
        repository_name
    )

    folder = os.path.join(
        REPOSITORY_ROOT,
        slug
    )

    os.makedirs(
        folder,
        exist_ok=True
    )

    metadata = {

        "repository_name": repository_name,

        "base_url": base_url,

        "status": "Building",

        "article_count": 0

    }

    with open(

        os.path.join(
            folder,
            "metadata.json"
        ),

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(
            metadata,
            file,
            indent=4
        )

    register_repository(

        repository_name,

        base_url,

        folder

    )

    return folder