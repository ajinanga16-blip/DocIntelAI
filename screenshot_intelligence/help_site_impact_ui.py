import streamlit as st

from workflows.screenshot_analysis_workflow import (
    analyze_screenshot_workflow
)

from workflows.discover_impacted_articles_workflow import (
    discover_impacted_articles
)

from workflows.discover_impacted_articles_v2_workflow import (
    discover_impacted_articles_v2
)

from workflows.generate_documentation_impact_workflow import (
    generate_documentation_impact
)

from ui.discovery_results_ui import (
    render_discovery_results
)

from utils.excel_exporter import (
    export_inventory
)


def render_help_site_impact():

    st.subheader(
        "Help Site Impact Analysis"
    )

    search_engine = st.radio(

        "Search Engine",

        [
            "Classic Search (V1)",
            "AI Candidate Search (V2)"
        ],

        horizontal=True

    )

    screenshot_file = st.file_uploader(

        "Upload Screenshot",

        type=[
            "png",
            "jpg",
            "jpeg"
        ],

        key="help_site_screenshot"

    )

    help_site_url = st.text_input(
        "Help Site URL"
    )

    if screenshot_file:

        st.image(
            screenshot_file,
            use_container_width=True
        )

    if screenshot_file and help_site_url:

        if st.button(
            "🔍 Discover Impacted Articles"
        ):

            with st.spinner(
                "Analyzing Screenshot..."
            ):

                screenshot_context = (
                    analyze_screenshot_workflow(
                        screenshot_file
                    )
                )

            with st.spinner(
                "Searching Help Site..."
            ):

                if search_engine == "Classic Search (V1)":

                    results = discover_impacted_articles(
                        help_site_url,
                        screenshot_context
                    )

                else:

                    results = discover_impacted_articles_v2(
                        help_site_url,
                        screenshot_context
                    )

            #
            # Save inventory if workflow returns it
            #

            st.session_state[
                "inventory"
            ] = results.get(
                "inventory",
                []
            )

            st.session_state[
                "matched_articles"
            ] = results.get(
                "matched_articles",
                []
            )

            st.session_state.pop(
                "documentation_impact",
                None
            )

    #
    # Export inventory
    #

    if (
        "inventory" in st.session_state
        and
        st.session_state["inventory"]
    ):

        inventory_excel = export_inventory(

            st.session_state[
                "inventory"
            ]

        )

        st.download_button(

            "⬇ Export Complete Inventory",

            inventory_excel,

            file_name="inventory.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        )

    #
    # Review Articles
    #

    if "matched_articles" in st.session_state:

        selected_articles = render_discovery_results(

            st.session_state[
                "matched_articles"
            ]

        )

        if selected_articles:

            if st.button(
                "📝 Generate Documentation Impact"
            ):

                with st.spinner(
                    "Generating Documentation Impact..."
                ):

                    impacts = (
                        generate_documentation_impact(
                            screenshot_file,
                            selected_articles
                        )
                    )

                st.session_state[
                    "documentation_impact"
                ] = impacts

    #
    # Documentation Impact
    #

    if "documentation_impact" in st.session_state:

        impacts = st.session_state[
            "documentation_impact"
        ]

        st.divider()

        st.header(
            "Documentation Impact"
        )

        for article in impacts:

            with st.expander(
                article["title"]
            ):

                st.markdown(
                    f"**URL:** {article['url']}"
                )

                st.markdown(
                    article["impact"]
                )

        st.divider()

        st.success(
            f"Completed analysis for {len(impacts)} article(s)."
        )