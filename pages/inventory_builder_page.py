import streamlit as st

from workflows.build_inventory_v2_workflow import (
    build_inventory_workflow_v2
)

from utils.excel_exporter import (
    export_inventory
)


def show_page():

    st.title(
        "📚 Documentation Inventory Builder"
    )

    st.write(
        """
Build a reusable documentation inventory.

The inventory can later be used by:

• Screenshot Intelligence

• JIRA Intelligence

• Knowledge Gap Analyzer

• Impact Analysis
"""
    )

    help_site_url = st.text_input(
        "Help Site URL"
    )

    if st.button(
        "🚀 Build Inventory"
    ):

        with st.spinner(
            "Building inventory..."
        ):

            inventory = (
                build_inventory_workflow_v2(
                    help_site_url
                )
            )

        st.success(
            f"Inventory Built: {len(inventory)} articles"
        )

        excel = export_inventory(
            inventory
        )

        st.download_button(

            "⬇ Export Inventory",

            excel,

            file_name="inventory.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        )

        st.dataframe(
            inventory,
            use_container_width=True
        )