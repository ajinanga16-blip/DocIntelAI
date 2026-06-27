import json
from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOBS_FOLDER = PROJECT_ROOT / "data" / "jobs"


def show_page():

    st.title("⚙ Job Manager")

    st.write(
        """
        Monitor long-running jobs across the DocIntel AI platform.
        """
    )

    jobs = []

    if JOBS_FOLDER.exists():

        for job_file in JOBS_FOLDER.glob("*.json"):

            with open(job_file, "r", encoding="utf-8") as file:

                jobs.append(json.load(file))

    if not jobs:

        st.info("No jobs found.")

        return

    jobs.sort(
        key=lambda job: job["created_at"],
        reverse=True
    )

    dataframe = pd.DataFrame(jobs)

    display_columns = [
        "job_type",
        "status",
        "progress",
        "message",
        "created_at",
        "updated_at"
    ]

    st.dataframe(
        dataframe[display_columns],
        use_container_width=True,
        hide_index=True
    )