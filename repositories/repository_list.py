from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

REPOSITORIES_FOLDER = PROJECT_ROOT / "data" / "repositories"


def get_repository_names():
    """
    Return all repository names.
    """

    if not REPOSITORIES_FOLDER.exists():
        return []

    repositories = []

    for folder in REPOSITORIES_FOLDER.iterdir():

        if folder.is_dir():

            repositories.append(
                folder.name
            )

    repositories.sort()

    return repositories