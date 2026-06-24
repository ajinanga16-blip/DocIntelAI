import streamlit as st

from agents.documentation_url_fetcher import (
    fetch_documentation_content
)

from agents.screenshot_impact_agent import (
    analyze_documentation_impact
)

from screenshot_intelligence.ui_helpers import (
    render_download_buttons
)


def render_documentation_impact():

    screenshot_file = st.file_uploader(
        "Upload Screenshot",
        type=["png", "jpg", "jpeg"],
        key="impact_screenshot"
    )

    documentation_url = st.text_input(
        "Documentation URL"
    )

    if screenshot_file:

        st.image(
            screenshot_file,
            caption="Uploaded Screenshot",
            use_container_width=True
        )

    if screenshot_file and documentation_url:

        if st.button(
            "Analyze Documentation Impact"
        ):

            with st.spinner(
                "Fetching Documentation..."
            ):

                documentation_content = (
                    fetch_documentation_content(
                        documentation_url
                    )
                )

            with st.spinner(
                "Analyzing Documentation Impact..."
            ):

                st.session_state[
                    "impact_result"
                ] = analyze_documentation_impact(
                    screenshot_file,
                    documentation_content
                )

    if "impact_result" in st.session_state:

        result = st.session_state[
            "impact_result"
        ]

        st.markdown(result)

        render_download_buttons(
            result,
            "documentation_impact.txt",
            "documentation_impact.md"
        )