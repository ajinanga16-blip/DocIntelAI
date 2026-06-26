from workflows.refresh_repository_workflow import (
    refresh_repository
)
from repositories.repository_operations import (
    delete_repository
)
from utils.inventory_exporter import (
    export_inventory
)
import json
import os

import pandas as pd
import streamlit as st


def show_repository_details(
    repository
):

    st.subheader(
        repository["repository_name"]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Status",
            repository["status"]
        )

        st.metric(
            "Articles",
            repository["article_count"]
        )

    with col2:

        st.metric(
            "Last Updated",
            repository["last_updated"]
        )

    st.text_input(

        "Base URL",

        value=repository["base_url"],

        disabled=True

    )

    st.divider()

    inventory_file = os.path.join(

        repository["folder"],

        "inventory.json"

    )

    if os.path.exists(
        inventory_file
    ):

        with open(
            inventory_file,
            "r",
            encoding="utf-8"
        ) as file:

            inventory = json.load(
                file
            )

        st.subheader(
            "Inventory"
        )

        rows = []

        for article in inventory:

            rows.append({

                "Title": article.get(
                    "title",
                    ""
                ),

                "URL": article.get(
                    "url",
                    ""
                ),

                "Discovery": article.get(
                    "discovered_by",
                    ""
                )

            })

        st.dataframe(

            pd.DataFrame(rows),

            use_container_width=True,

            height=500

        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 Refresh Repository"
        ):

            with st.spinner(
                "Refreshing repository..."
            ):

                refresh_repository(
                    repository
                )

            st.success(
                "Repository refreshed successfully."
            )

            st.rerun()

        if st.button(
            "📤 Export Inventory"
        ):

            export_file = export_inventory(
                repository["folder"]
            )

            with open(
                export_file,
                "rb"
            ) as file:

                st.download_button(

                    "⬇ Download Inventory",

                    data=file,

                    file_name="inventory.xlsx",

                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                )

    with col2:

        if st.button(
            "🗑 Delete Repository"
        ):

            delete_repository(
                repository
            )

            if "selected_repository" in st.session_state:

                del st.session_state[
                    "selected_repository"
             ]

            st.success(
                "Repository deleted successfully."
            )

            st.rerun()

        st.button(
            "🧠 Build Knowledge Index",
            disabled=True
        )