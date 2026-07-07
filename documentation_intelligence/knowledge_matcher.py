def flatten_metadata(value):
    """
    Convert any metadata into searchable text.

    Supports:
    - string
    - list of strings
    - dictionary
    - list of dictionaries
    - nested structures
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


def calculate_match_score(
    article,
    ticket
):
    """
    Weighted Repository Matcher.

    Stage 1 of Documentation Intelligence.

    Returns a weighted score used for
    candidate selection.
    """

    score = 0

    #
    # Ticket Context
    #

    ticket_text = " ".join([

        ticket.get(
            "summary",
            ""
        ),

        ticket.get(
            "description",
            ""
        ),

        ticket.get(
            "resolution",
            ""
        ),

        ticket.get(
            "module",
            ""
        )

    ]).lower()

    words = []

    for word in ticket_text.split():

        word = word.strip()

        if len(word) >= 4:

            words.append(word)

    #
    # Matching Weights
    #

    weights = {

        "title": 40,

        "description": 25,

        "features": 20,

        "tasks": 15,

        "keywords": 10,

        "error_topics": 10,

        "ui_elements": 5,

        "category": 5

    }

    #
    # Title
    #

    title = flatten_metadata(
        article.get(
            "title",
            ""
        )
    ).lower()

    for word in words:

        if word in title:

            score += weights["title"]

    #
    # Description
    #

    description = flatten_metadata(
        article.get(
            "description",
            ""
        )
    ).lower()

    for word in words:

        if word in description:

            score += weights["description"]

    #
    # Category
    #

    category = flatten_metadata(
        article.get(
            "category",
            ""
        )
    ).lower()

    for word in words:

        if word in category:

            score += weights["category"]

    #
    # Features
    #

    features = flatten_metadata(

        article.get(
            "features",
            []
        )

    ).lower()

    for word in words:

        if word in features:

            score += weights["features"]

    #
    # Tasks
    #

    tasks = flatten_metadata(

        article.get(
            "tasks",
            []
        )

    ).lower()

    for word in words:

        if word in tasks:

            score += weights["tasks"]

    #
    # Keywords
    #

    keywords = flatten_metadata(

        article.get(
            "keywords",
            []
        )

    ).lower()

    for word in words:

        if word in keywords:

            score += weights["keywords"]

    #
    # Error Topics
    #

    errors = flatten_metadata(

        article.get(
            "error_topics",
            []
        )

    ).lower()

    for word in words:

        if word in errors:

            score += weights["error_topics"]

    #
    # UI Elements
    #

    ui = flatten_metadata(

        article.get(
            "ui_elements",
            []
        )

    ).lower()

    for word in words:

        if word in ui:

            score += weights["ui_elements"]

    return score