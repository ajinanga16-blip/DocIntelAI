from documentation_intelligence.text_normalizer import (
    normalize_text
)

from documentation_intelligence.knowledge_context_builder import (
    build_search_context
)


def flatten_metadata(value):
    """
    Flattens nested metadata into searchable text.
    """

    if value is None:
        return ""

    if isinstance(value, str):
        return value

    if isinstance(value, dict):

        parts = []

        for item in value.values():

            parts.append(
                flatten_metadata(item)
            )

        return " ".join(parts)

    if isinstance(value, list):

        parts = []

        for item in value:

            parts.append(
                flatten_metadata(item)
            )

        return " ".join(parts)

    return str(value)


def tokenize(text):
    """
    Normalize and tokenize text.
    """

    text = normalize_text(text)

    tokens = []

    for word in text.split():

        word = word.strip()

        if len(word) >= 3:

            tokens.append(word)

    return set(tokens)


def overlap_score(
    search_tokens,
    article_tokens,
    weight
):
    """
    Calculates weighted overlap.
    """

    overlap = (
        search_tokens &
        article_tokens
    )

    if not overlap:

        return 0

    return len(overlap) * weight


def build_article_index(article):
    """
    Build normalized searchable fields.
    """

    return {

        "title": tokenize(
            article.get(
                "title",
                ""
            )
        ),

        "description": tokenize(
            flatten_metadata(
                article.get(
                    "description",
                    ""
                )
            )
        ),

        "features": tokenize(
            flatten_metadata(
                article.get(
                    "features",
                    []
                )
            )
        ),

        "tasks": tokenize(
            flatten_metadata(
                article.get(
                    "tasks",
                    []
                )
            )
        ),

        "keywords": tokenize(
            flatten_metadata(
                article.get(
                    "keywords",
                    []
                )
            )
        ),

        "error_topics": tokenize(
            flatten_metadata(
                article.get(
                    "error_topics",
                    []
                )
            )
        ),

        "ui_elements": tokenize(
            flatten_metadata(
                article.get(
                    "ui_elements",
                    []
                )
            )
        ),

        "category": tokenize(
            article.get(
                "category",
                ""
            )
        )

    }
def calculate_match_score(
    article,
    context
):
    """
    Documentation Intelligence Matcher

    Shared by:
    - Gap Analysis
    - Screenshot Intelligence
    - Impact Analysis
    """

    #
    # Build search context
    #

    search_text = build_search_context(
        context
    )

    search_tokens = tokenize(
        search_text
    )

    article_index = build_article_index(
        article
    )

    score = 0

    #
    # Weighted scoring
    #

    weights = {

        "title": 50,
        "description": 25,
        "features": 20,
        "tasks": 20,
        "keywords": 20,
        "error_topics": 15,
        "ui_elements": 15,
        "category": 10

    }

    for field, weight in weights.items():

        score += overlap_score(

            search_tokens,

            article_index[field],

            weight

        )

    #
    # Screenshot Intelligence bonuses
    #

    primary_screen = normalize_text(

        context.get(
            "primary_screen",
            ""
        )

    )

    primary_action = normalize_text(

        context.get(
            "primary_action",
            ""
        )

    )

    title_text = normalize_text(

        article.get(
            "title",
            ""
        )

    )

    if primary_screen:

        if primary_screen in title_text:

            score += 75

    if primary_action:

        if primary_action in title_text:

            score += 50

    #
    # Navigation bonus
    #

    for item in context.get(

        "navigation_path",

        []

    ):

        item = normalize_text(item)

        if item in title_text:

            score += 20

    #
    # Important keyword bonus
    #

    for keyword in context.get(

        "important_keywords",

        []

    ):

        keyword = normalize_text(keyword)

        if keyword in title_text:

            score += 15

    #
    # Require minimum confidence
    #

    return score