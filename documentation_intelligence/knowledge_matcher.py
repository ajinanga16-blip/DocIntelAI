from documentation_intelligence.text_normalizer import (
    normalize_text
)
from documentation_intelligence.knowledge_context_builder import (
    build_search_context
)


def flatten_metadata(value):
    """
    Convert any metadata into searchable text.
    """

    if value is None:
        return ""

    if isinstance(value, str):
        return value

    if isinstance(value, dict):
        return " ".join(
            flatten_metadata(v)
            for v in value.values()
        )

    if isinstance(value, list):
        return " ".join(
            flatten_metadata(v)
            for v in value
        )

    return str(value)


def calculate_match_score(
    article,
    context
):
    """
    Generic weighted matcher for all
    Documentation Intelligence modules.
    """

    score = 0

    context_text = build_search_context(
        context
    )

    words = []

    for word in context_text.split():

        word = word.strip().lower()

        if len(word) >= 3:
            words.append(word)

    weights = {

        "title": 40,
        "description": 25,
        "features": 20,
        "tasks": 15,
        "keywords": 15,
        "error_topics": 10,
        "ui_elements": 10,
        "category": 5

    }

    searchable_fields = {

        "title": article.get("title", ""),
        "description": article.get("description", ""),
        "features": article.get("features", []),
        "tasks": article.get("tasks", []),
        "keywords": article.get("keywords", []),
        "error_topics": article.get("error_topics", []),
        "ui_elements": article.get("ui_elements", []),
        "category": article.get("category", "")

    }

    for field, value in searchable_fields.items():

        text = normalize_text(
            flatten_metadata(value)
        )

        for word in words:

            word = normalize_text(word)
            if word in text:
                score += weights[field]

    if article.get("title") == "Adding a Template to Your Workspace | Savant Labs, Inc. Help Center":
        print("=" * 60)
        print(article.get("title"))
        print("Score:", score)
        print("Keywords:", article.get("keywords"))
        print("Features:", article.get("features"))
        print("=" * 60)

    return score