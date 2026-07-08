def build_screen_context(screen_data):
    """
    Converts screenshot analysis into a normalized
    screen context for Documentation Intelligence.
    """

    page_title = screen_data.get("page_title", "").strip()
    screen_name = screen_data.get("screen_name", "").strip()

    breadcrumbs = screen_data.get("breadcrumbs", [])
    buttons = screen_data.get("buttons", [])
    labels = screen_data.get("labels", [])
    menus = screen_data.get("menus", [])
    keywords = screen_data.get("keywords", [])

    #
    # Primary screen
    #

    primary_screen = screen_name or page_title

    #
    # Primary action
    #

    primary_action = ""

    priority_actions = [
        "add",
        "create",
        "edit",
        "delete",
        "import",
        "export",
        "template",
        "templates",
        "run",
        "runs",
        "analysis",
        "analyses",
        "dataset",
        "workflow",
        "publish"
    ]

    search_space = (
        buttons +
        labels +
        menus +
        keywords
    )

    for item in search_space:

        text = str(item).lower()

        for action in priority_actions:

            if action in text:
                primary_action = item
                break

        if primary_action:
            break

    #
    # Important keywords
    #

    important_keywords = []

    if page_title:
        important_keywords.append(page_title)

    if screen_name:
        important_keywords.append(screen_name)

    important_keywords.extend(keywords)

    #
    # Secondary context
    #

    ui_context = []

    ui_context.extend(buttons)
    ui_context.extend(labels)
    ui_context.extend(menus)

    #
    # Navigation path
    #

    navigation_path = breadcrumbs.copy()

    if screen_name:
        navigation_path.append(screen_name)

    if primary_action:
        navigation_path.append(primary_action)

    #
    # User intent
    #

    user_intent = ""

    if primary_action:

        user_intent = f"{primary_action} on {primary_screen}"

    else:

        user_intent = primary_screen

    return {

        "primary_screen": primary_screen,

        "primary_action": primary_action,

        "navigation_path": navigation_path,

        "important_keywords": important_keywords,

        "secondary_keywords": keywords,

        "ui_context": ui_context,

        "user_intent": user_intent

    }