import streamlit as st

from workflows.build_inventory_v2_workflow import (
    build_inventory_workflow_v2
)

from job_engine.background_runner import (
    run_in_background
)


def show_page():

    st.title("🧭 Documentation Discovery")

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

    notification_email = st.text_input(
        "Notification Email",
        placeholder="name@company.com"
    )

    st.info(
        """
        **Note**

        Repository builds now run in the background.

        You may leave this page after starting a build.

        Track progress in **⚙ Job Manager**.

        Email notifications will be enabled in the next step.
        """
    )

    if st.button("🚀 Build Repository"):

        if not repository_name:

            st.error("Please enter a Repository Name.")

            return

        if not documentation_url:

            st.error("Please enter a Documentation URL.")

            return

        if not notification_email:

            st.error("Please enter a Notification Email.")

            return

        run_in_background(
            build_inventory_workflow_v2,
            repository_name,
            documentation_url,
            notification_email
        )

        st.success(
            """
Repository build started successfully.

You may leave this page.

Track progress in **⚙ Job Manager**.

You will receive an email when the build completes.
"""
        )