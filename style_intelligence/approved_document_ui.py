import streamlit as st

from shared.export_center.export_center import (
    render_export_center
)


def render_approved_document(
    approved_document,
    document_title
):
    """
    Render the approved document and
    provide export options.
    """

    if not approved_document:

        return

    st.divider()

    st.subheader(
        "✅ Approved Document"
    )

    st.metric(
        "Final Compliance Score",
        approved_document["score"]
    )

    st.markdown(
        approved_document["document"]
    )

    render_export_center(

        title=f"{document_title} - Approved",

        content=approved_document["document"]

    )