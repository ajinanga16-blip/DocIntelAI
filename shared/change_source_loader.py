import streamlit as st

from shared.change_sources.csv_source import (
    render_csv_source
)

from shared.change_sources.excel_source import (
    render_excel_source
)

from shared.change_sources.jira_source import (
    render_jira_source
)

def render_change_source_loader():

    source_type = st.radio(
        "Source Type",
        [
            "CSV",
            "Excel",
            "JIRA",
    
            "Release Notes",
            "Manual Input"
        ]
    )

    data = {
        "source_type": source_type,
        "uploaded_file": None,
        "ticket_ids": [],
        "jql": "",
        "sprint": "",
        "epic": "",
        "release_notes": "",
        "manual_input": ""
    }

    if source_type == "CSV":

        data = render_csv_source(data)

    elif source_type == "Excel":

        data = render_excel_source(data)

    elif source_type == "JIRA":

        data = render_jira_source(data)

    elif source_type == "Release Notes":

        data["release_notes"] = st.text_area(
            "Paste Release Notes",
            height=200
        )

    elif source_type == "Manual Input":

        data["manual_input"] = st.text_area(
            "Describe the Product Change",
            height=200
        )

    return data