import streamlit as st

from agents.screenshot_comparison_agent import (
    compare_screenshots
)

from screenshot_intelligence.ui_helpers import (
    render_download_buttons
)


def render_compare_screenshots():

    old_screenshot = st.file_uploader(
        "Upload Existing Screenshot",
        type=["png", "jpg", "jpeg"],
        key="old_screenshot"
    )

    new_screenshot = st.file_uploader(
        "Upload New Screenshot",
        type=["png", "jpg", "jpeg"],
        key="new_screenshot"
    )

    if old_screenshot and new_screenshot:

        col1, col2 = st.columns(2)

        with col1:

            st.image(
                old_screenshot,
                caption="Existing Screenshot",
                use_container_width=True
            )

        with col2:

            st.image(
                new_screenshot,
                caption="New Screenshot",
                use_container_width=True
            )

        if st.button(
            "Compare Screenshots"
        ):

            with st.spinner(
                "Comparing Screenshots..."
            ):

                st.session_state[
                    "comparison_result"
                ] = compare_screenshots(
                    old_screenshot,
                    new_screenshot
                )

    if "comparison_result" in st.session_state:

        result = st.session_state[
            "comparison_result"
        ]

        st.markdown(result)

        render_download_buttons(
            result,
            "screenshot_comparison.txt",
            "screenshot_comparison.md"
        )