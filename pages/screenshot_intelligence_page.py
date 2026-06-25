import streamlit as st

from screenshot_intelligence.analyze_screenshot_ui import (
    render_analyze_screenshot
)

from screenshot_intelligence.compare_screenshots_ui import (
    render_compare_screenshots
)

from screenshot_intelligence.documentation_impact_ui import (
    render_documentation_impact
)

from screenshot_intelligence.help_site_impact_ui import (
    render_help_site_impact
)

from ui.screenshot_article_results import (
    render_article_results
)

def show_page():

    st.title("📸 Screenshot Intelligence")

    analysis_type = st.radio(
        "Choose a Screenshot Intelligence Capability",
        [
            "Analyze Screenshot",
            "Compare Screenshots",
            "Documentation Impact",
            "Help Site Impact"
        ]
    )

    if analysis_type == "Analyze Screenshot":

        render_analyze_screenshot()

    elif analysis_type == "Compare Screenshots":

        render_compare_screenshots()

    elif analysis_type == "Documentation Impact":

        render_documentation_impact()
    
    elif analysis_type == "Help Site Impact":

        render_help_site_impact()

