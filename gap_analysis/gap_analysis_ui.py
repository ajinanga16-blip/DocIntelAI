import streamlit as st

from repositories.repository_list import (
    get_repository_names
)

from gap_analysis.work_item_loader import (
    render_work_item_loader
)

from workflows.gap_analysis_job import (
    run_gap_analysis_job
)

from job_engine.background_runner import (
    run_in_background
)


def render_gap_analysis():

    st.title("🔍 Knowledge Gap Analysis")

    repositories = get_repository_names()

    if not repositories:

        st.warning(
            "No repositories found. Please build a repository first."
        )

        return

    repository_name = st.selectbox(

        "Repository",

        repositories

    )

    tickets = render_work_item_loader()

    if not tickets:

        return

    if st.button(

        "Analyze Gap",

        width="stretch"

    ):

        run_in_background(

            run_gap_analysis_job,

            repository_name,

            tickets

        )

        st.success(

            "Gap Analysis started successfully."

        )

        st.info(

            """
The analysis is now running in the background.

You can continue using DocIntel AI.

Monitor progress from **Job Manager**.

When the job completes, click **Open Documentation Action Plan**.
            """

        )