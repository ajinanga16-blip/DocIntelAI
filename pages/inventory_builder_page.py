import streamlit as st

from workflows.build_inventory_v2_workflow import (
    build_inventory_workflow_v2
)


def show_page():

    st.title(
        "🧭 Documentation Discovery"
    )

    st.write(
        """
        Build a reusable documentation repository.

        This is a one-time process for each documentation site.
        Once completed, all DocIntel AI modules will use this repository.
        """
    )

    repository_name = st.text_input(
        "Repository Name",
        placeholder="Example: Savant Documentation"
    )

    documentation_url = st.text_input(
        "Documentation URL",
        placeholder="https://docs.company.com"
    )

    st.info(
        """
        **Note**

        Large documentation sites (500+ articles) may take several minutes
        to process during the initial build.

        This is a one-time activity.

        Future updates will use the saved repository.
        """
    )

    if st.button(
        "🚀 Build Repository"
    ):

        if not repository_name:

            st.error(
                "Please enter a Repository Name."
            )
            return

        if not documentation_url:

            st.error(
                "Please enter a Documentation URL."
            )
            return

        with st.spinner(
            "Building repository..."
        ):

            inventory = build_inventory_workflow_v2(
                repository_name,
                documentation_url
            )

        st.success(
            f"Repository built successfully.\n\n"
            f"Articles discovered: {len(inventory)}"
        )