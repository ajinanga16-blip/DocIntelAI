import streamlit as st

from repositories.repository_registry import (
    get_repositories
)

from pages.repository_details_page import (
    show_repository_details
)


def show_page():

    st.title(
        "🗂 Documentation Repositories"
    )

    repositories = get_repositories()

    if not repositories:

        st.info(
            "No repositories available."
        )

        return

    for repo in repositories:

        with st.container():

            st.subheader(
                repo["repository_name"]
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"**Status:** {repo['status']}"
                )

            with col2:

                st.write(
                    f"**Articles:** {repo['article_count']}"
                )

            with col3:

                st.write(
                    f"**Updated:** {repo['last_updated']}"
                )

            if st.button(
                "📂 Open Repository",
                key=repo["repository_id"]
            ):

                st.session_state[
                    "selected_repository"
                ] = repo

            st.divider()

    #
    # Repository Details
    #

    if (
        "selected_repository"
        in st.session_state
    ):

        st.markdown("---")

        show_repository_details(

            st.session_state[
                "selected_repository"
            ]

        )