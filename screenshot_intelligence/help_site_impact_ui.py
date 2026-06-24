import streamlit as st

from agents.help_site_impact_agent import (
    analyze_help_site_impact
)

from agents.documentation_url_fetcher import (
    fetch_documentation_content
)

from screenshot_intelligence.ui_helpers import (
    render_download_buttons
)


def render_help_site_impact():

    screenshot_file = st.file_uploader(
        "Upload Screenshot",
        type=["png", "jpg", "jpeg"],
        key="help_site_screenshot"
    )

    help_site_url = st.text_input(
        "Help Site URL"
    )

    if screenshot_file:

        st.image(
            screenshot_file,
            caption="Uploaded Screenshot",
            use_container_width=True
        )

    if screenshot_file and help_site_url:

        if st.button(
            "Analyze Help Site Impact"
        ):

            with st.spinner(
                "Fetching Help Site Content..."
            ):

                site_content = (
                    fetch_documentation_content(
                        help_site_url
                    )
                )

            with st.spinner(
                "Analyzing Help Site Impact..."
            ):

                st.session_state[
                    "help_site_result"
                ] = analyze_help_site_impact(
                    screenshot_file,
                    site_content
                )

    if "help_site_result" in st.session_state:

        result = st.session_state[
            "help_site_result"
        ]

        st.markdown(result)

        render_download_buttons(
            result,
            "help_site_impact.txt",
            "help_site_impact.md"
        )