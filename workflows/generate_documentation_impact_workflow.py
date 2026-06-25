from agents.help_site_impact_agent import (
    analyze_help_site_impact
)


def generate_documentation_impact(
    screenshot_file,
    selected_articles
):
    """
    Step 2:
    Generate documentation impact
    only for writer-selected articles.
    """

    return analyze_help_site_impact(
        screenshot_file,
        selected_articles
    )