import json
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent

JOBS_FOLDER = PROJECT_ROOT / "data" / "jobs"


def show_page():

    st.title("⚙ Job Manager")

    st.write(
        "Monitor background jobs across the DocIntel AI platform."
    )

    if not JOBS_FOLDER.exists():

        st.info(
            "No jobs found."
        )

        return

    jobs = []

    for job_file in JOBS_FOLDER.glob("*.json"):

        with open(
            job_file,
            "r",
            encoding="utf-8"
        ) as file:

            jobs.append(
                json.load(file)
            )

    if not jobs:

        st.info(
            "No jobs found."
        )

        return

    jobs.sort(

        key=lambda x: x.get(
            "created_at",
            ""
        ),

        reverse=True

    )

    for job in jobs:

        with st.container(border=True):

            left, right = st.columns(
                [4, 1]
            )

            with left:

                st.subheader(
                    job.get(
                        "job_type",
                        ""
                    )
                )

                repository = job.get(
                    "repository_name",
                    ""
                )

                if repository:

                    st.caption(
                        f"Repository: {repository}"
                    )

            with right:

                status = job.get(
                    "status",
                    ""
                )

                if status == "Completed":

                    st.success(
                        status
                    )

                elif status == "Running":

                    st.warning(
                        status
                    )

                elif status == "Failed":

                    st.error(
                        status
                    )

                else:

                    st.info(
                        status
                    )

            progress = job.get(
                "progress",
                0
            )

            st.progress(
                progress / 100
            )

            current = job.get(
                "current_step",
                0
            )

            total = job.get(
                "total_steps",
                0
            )

            if total:

                st.write(
                    f"Progress: {current}/{total}"
                )

            phase = job.get(
                "current_phase",
                ""
            )

            if phase:

                st.write(
                    f"Current Phase: {phase}"
                )

            item = job.get(
                "current_item",
                ""
            )

            if item:

                st.write(
                    f"Current Item: {item}"
                )

            st.caption(

                job.get(
                    "message",
                    ""
                )

            )

            #
            # Future Result Links
            #

            if job.get(
                "result_available",
                False
            ):

                if st.button(

                    f"Open {job.get('result_type','Result')}",

                    key=f"open_{job['job_id']}"

                ):

                    st.session_state["selected_job_id"] = job["job_id"]

                    st.session_state["selected_page"] = "Job Result"

                    st.rerun()

            st.divider()

    st.info(

        "Background jobs continue running even if you navigate to another page."

    )