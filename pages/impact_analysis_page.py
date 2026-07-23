import streamlit as st

from shared.change_source_loader import (
    render_change_source_loader
)

from shared.work_item_service import (
    load_work_items
)

from repositories.repository_list import (
    get_repository_names
)

from workflows.impact_analysis_job import (
    run_impact_analysis_job
)

from job_engine.background_runner import (
    run_in_background
)


def render_impact_analysis():

    st.title("⚡ Impact Analysis")

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

    source = render_change_source_loader()

    work_items = []

    if source["source_type"] in ["CSV", "Excel"]:

        if source["uploaded_file"]:

            work_items = load_work_items(source)

    elif source["source_type"] == "JIRA":

        if (
            source["ticket_ids"]
            or source["jql"]
            or source["sprint"]
            or source["epic"]
        ):

            work_items = load_work_items(source)

    elif source["source_type"] == "Release Notes":

        if source["release_notes"]:

            work_items = load_work_items(source)

    elif source["source_type"] == "Manual Input":

        if source["manual_input"]:

            work_items = load_work_items(source)

    if not work_items:

        return

    

       
    st.divider()

    if st.button(
        "Analyze Impact",
        type="primary",
        use_container_width=True
    ):

        run_in_background(

            run_impact_analysis_job,

            repository_name,

            work_items

        )

        st.success(
            "Impact Analysis started successfully."
        )

        st.info(
            """
    The analysis is now running in the background.

    You can continue using DocIntel AI.

    Monitor progress from **Job Manager**.
            """
        )

    st.subheader("Results")

    st.info(
        "Impact analysis results will appear here."
    )