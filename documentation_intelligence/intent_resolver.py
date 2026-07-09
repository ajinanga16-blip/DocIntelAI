from documentation_intelligence.text_normalizer import (
    normalize_text
)


def resolve_user_intent(context):
    """
    Converts screenshot context into
    a deterministic user intent.

    Shared by:
    - Screenshot Intelligence
    - Gap Analysis
    - Impact Analysis
    """

    menus = context.get("menus", [])
    buttons = context.get("buttons", [])
    labels = context.get("labels", [])

    workflow = ""

    #
    # Priority
    #

    priority = [

        "templates",
        "template",
        "runs",
        "run",
        "analysis",
        "analyses",
        "datasets",
        "dataset",
        "sources",
        "source",
        "destinations",
        "destination",
        "admin"

    ]

    search_space = []

    search_space.extend(menus)
    search_space.extend(buttons)
    search_space.extend(labels)

    for item in search_space:

        text = normalize_text(item)

        for keyword in priority:

            if keyword in text:

                workflow = keyword.title()

                break

        if workflow:

            break

    #
    # Intent
    #

    if workflow == "Templates":

        primary_intent = "Manage Templates"

    elif workflow in [

        "Analysis",
        "Analyses"

    ]:

        primary_intent = "Manage Analyses"

    elif workflow == "Runs":

        primary_intent = "Manage Runs"

    elif workflow == "Sources":

        primary_intent = "Manage Sources"

    elif workflow == "Destinations":

        primary_intent = "Manage Destinations"

    else:

        primary_intent = context.get(

            "user_intent",

            ""

        )

    return {

        "primary_intent": primary_intent,

        "workflow": workflow

    }