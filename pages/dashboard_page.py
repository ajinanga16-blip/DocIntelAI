import streamlit as st


def _open_page(page_name):
    """
    Navigate to another application page.
    """

    st.session_state.selected_page = page_name

    st.rerun()


def _render_feature_card(
    icon,
    title,
    description,
    page_name
):
    """
    Render one consistent dashboard feature card.
    """

    with st.container(
        border=True
    ):

        st.markdown(
            f"""
            <div style="
                min-height: 58px;
                display: flex;
                align-items: flex-start;
            ">
                <h2 style="
                    margin: 0;
                    font-size: 1.55rem;
                    line-height: 1.2;
                ">
                    {icon} {title}
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                min-height: 72px;
                display: flex;
                align-items: flex-start;
            ">
                <p style="
                    margin: 0;
                    font-size: 1rem;
                    line-height: 1.5;
                ">
                    {description}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Open →",
            key=f"dashboard_card_{page_name}",
            width="stretch"
        ):

            _open_page(
                page_name
            )


def render_dashboard():

    #
    # Header
    #

    st.title(
        "📚 DocIntel AI"
    )

    st.subheader(
        "Documentation Intelligence Platform"
    )

    #st.write(
    #    "Analyze, create, review, and improve "
    #    "product documentation from one workspace."
    #)
    #
    #st.divider()

    #
    # Primary Intelligence Modules
    #

    #st.header(
    #    "Intelligence Workspace"
    #)

    st.caption(
        "Choose a capability to get started."
    )

    #
    # First row — three primary capabilities
    #

    col1, col2, col3 = st.columns(
        3,
        gap="medium"
    )

    with col1:

        _render_feature_card(

            icon="📝",

            title="Create Docs",

            description=(
                "Create structured documentation "
                "from product changes and source content."
            ),

            page_name="Generate Docs"

        )

    with col2:

        _render_feature_card(

            icon="✍️",

            title="Review UX",

            description=(
                "Review product microcopy "
                "against UX writing style guides."
            ),

            page_name="UX Intelligence"

        )

    with col3:

        _render_feature_card(

            icon="🔎",

            title="Find Gaps",

            description=(
                "Identify missing, outdated, duplicate, "
                "and incomplete documentation."
            ),

            page_name="Gap Analysis"

        )

    #
    # Second row — full-width screen analysis
    #

    st.markdown(
        "<div style='height: 16px;'></div>",
        unsafe_allow_html=True
    )

    _render_feature_card(

        icon="🖼",

        title="Analyze Screens",

        description=(
            "Analyze product screens and identify "
            "UI elements for documentation intelligence."
        ),

        page_name="Screenshot Intelligence"

    )

    #
    # --------------------------------------------------
    # More Intelligence
    #
    # Temporarily hidden.
    # Keep this section for future use.
    # --------------------------------------------------
    #

    # st.divider()

    # st.header(
    #     "More Intelligence"
    # )

    # st.caption(
    #     "Additional documentation operations "
    #     "capabilities available in DocIntel AI."
    # )

    # col5, col6, col7 = st.columns(
    #     3,
    #     gap="medium"
    # )

    # with col5:

    #     with st.container(
    #         border=True
    #     ):

    #         st.markdown(
    #             "### 💥 Impact Analysis"
    #         )

    #         st.write(
    #             "Identify documentation affected "
    #             "by product and release changes."
    #         )

    #         if st.button(
    #             "Open →",
    #             key="dashboard_card_impact_analysis",
    #             width="stretch"
    #         ):

    #             _open_page(
    #                 "Impact Analysis"
    #             )

    # with col6:

    #     with st.container(
    #         border=True
    #     ):

    #         st.markdown(
    #             "### 🔗 Connect Documentation"
    #         )

    #         st.write(
    #             "Connect documentation repositories "
    #             "and build a documentation inventory."
    #         )

    #         if st.button(
    #             "Open →",
    #             key="dashboard_card_connect_documentation",
    #             width="stretch"
    #         ):

    #             _open_page(
    #                 "🔗 Connect Documentation"
    #             )

    # with col7:

    #     with st.container(
    #         border=True
    #     ):

    #         st.markdown(
    #             "### 📦 Repository Dashboard"
    #         )

    #         st.write(
    #             "Explore documentation repositories "
    #             "and their current content."
    #         )

    #         if st.button(
    #             "Open →",
    #             key="dashboard_card_repository_dashboard",
    #             width="stretch"
    #         ):

    #             _open_page(
    #                 "🗂 Repository Dashboard"
    #             )