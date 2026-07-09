import streamlit as st

from workflows.screenshot_analysis_workflow import (
    analyze_screenshot_workflow
)

from repositories.repository_list import (
    get_repository_names
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

    

    screenshot_file = st.file_uploader(

        "Upload Screenshot",

        type=[
            "png",
            "jpg",
            "jpeg"
        ],

        key="help_site_screenshot"

    )

    repositories = get_repository_names()

    repository_name = st.selectbox(
        "Repository",
        repositories,
        index=None,
        placeholder="Select a repository..."
    )

    if screenshot_file:

        st.image(
            screenshot_file,
            use_container_width=True
        )

    if screenshot_file and repository_name:

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

            progress = st.progress(0)

            status = st.empty()

            status.write("Stage 1/4 - Repository Search")

            progress.progress(25)

            results = discover_impacted_articles_v2(
                repository_name,
                screenshot_context
            )

            progress.progress(100)

            status.write("Completed")

            results = discover_impacted_articles_v2(
                repository_name,
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
                "recommended_articles"
            ] = results.get(
                "recommended_articles",
                []
            )

            st.session_state[
                "all_matches"
            ] = results.get(
                "all_matches",
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

    if "recommended_articles" in st.session_state:

        st.subheader("🎯 Top Recommended Articles")

        selected_articles = render_discovery_results(

            st.session_state[
                "recommended_articles"
            ],
            
            section="recommended"

        )

        with st.expander(

            f"Show all ranked matches ({len(st.session_state['all_matches'])})"

        ):

            render_discovery_results(

                st.session_state[
                    "all_matches"
                ],
                
                section="all_matches"

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