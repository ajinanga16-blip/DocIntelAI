import streamlit as st

from workflows.discover_impacted_articles_workflow import (
    discover_impacted_articles
)

from workflows.generate_documentation_impact_workflow import (
    generate_documentation_impact
)

from ui.discovery_results_ui import (
    render_discovery_results
)

from screenshot_intelligence.ui_helpers import (
    render_download_buttons
)


def render_help_site_impact():

    st.subheader(
        "Help Site Impact Analysis"
    )

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

    #
    # STEP 1
    #

    if (
        screenshot_file
        and help_site_url
    ):

        if st.button(
            "🔍 Discover Impacted Articles"
        ):

            #
            # Temporary placeholder
            # Replace with Screenshot Change JSON
            #

            screenshot_change = {
                "added_elements": [],
                "removed_elements": [],
                "navigation_changes": []
            }

            with st.spinner(
                "Discovering impacted articles..."
            ):

                results = (
                    discover_impacted_articles(
                        help_site_url,
                        screenshot_change
                    )
                )

            st.session_state[
                "discovered_articles"
            ] = results.get(
                "matched_articles",
                []
            )

    #
    # STEP 2
    #

    if (
        "discovered_articles"
        in st.session_state
    ):

        selected_articles = (
            render_discovery_results(
                st.session_state[
                    "discovered_articles"
                ]
            )
        )

        #
        # STEP 3
        #

        if (
            selected_articles
            and st.button(
                "📝 Generate Documentation Impact"
            )
        ):

            with st.spinner(
                "Generating impact..."
            ):

                result = (
                    generate_documentation_impact(
                        screenshot_file,
                        selected_articles
                    )
                )

            st.session_state[
                "help_site_result"
            ] = result

    if (
        "help_site_result"
        in st.session_state
    ):

        result = st.session_state[
            "help_site_result"
        ]

        st.markdown(result)

        render_download_buttons(
            result,
            "help_site_impact.txt",
            "help_site_impact.md"
        )