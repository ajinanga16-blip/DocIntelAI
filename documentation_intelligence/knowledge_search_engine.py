from repositories.repository_loader import (
    load_repository_inventory
)

from documentation_intelligence.knowledge_matcher import (
    calculate_match_score
)


def search_repository(

    repository_name,

    ticket,

    top_k=10

):

    inventory = load_repository_inventory(
        repository_name
    )

    matches = []

    for article in inventory:

        score = calculate_match_score(

            article,

            ticket

        )

        if score:

            matches.append({

                "score": score,

                "article": article

            })

    matches.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return matches[:top_k]