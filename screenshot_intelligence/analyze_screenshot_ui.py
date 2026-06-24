import streamlit as st

from agents.screenshot_agent import (
    analyze_screenshot
)

from screenshot_intelligence.ui_helpers import (
    render_download_buttons
)


def render_analyze_screenshot():

    uploaded_file = st.file_uploader(
        "Upload Screenshot",
        type=["png", "jpg", "jpeg"],
        key="single_screenshot"
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Uploaded Screenshot",
            use_container_width=True
        )

        if st.button(
            "Analyze Screenshot"
        ):

            with st.spinner(
                "Analyzing Screenshot..."
            ):

                st.session_state[
                    "screenshot_result"
                ] = analyze_screenshot(
                    uploaded_file
                )

    if "screenshot_result" in st.session_state:

        result = st.session_state[
            "screenshot_result"
        ]

        st.markdown(result)

        render_download_buttons(
            result,
            "screenshot_analysis.txt",
            "screenshot_analysis.md"
        )