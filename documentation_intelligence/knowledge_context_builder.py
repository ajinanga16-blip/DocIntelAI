def build_search_context(context):
    """
    Build a normalized search context for all intelligence modules.

    Supports:
    - JIRA
    - Screenshot Intelligence
    - Future PRDs
    - Future Transcripts
    - Manual Input
    """

    fields = []

    candidate_fields = [
        # JIRA
        "summary",
        "description",
        "resolution",
        "module",

        # Screenshot
        "page_title",
        "screen_name",
        "breadcrumbs",
        "buttons",
        "labels",
        "menus",
        "ui_elements",
        "keywords",

        # Generic / Future
        "title",
        "features",
        "tasks",
        "category"
    ]

    for field in candidate_fields:

        value = context.get(field)

        if not value:
            continue

        if isinstance(value, list):
            fields.extend([str(v) for v in value])

        else:
            fields.append(str(value))

    return " ".join(fields).lower()