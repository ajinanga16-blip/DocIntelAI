import streamlit as st

from generate_docs.generation_ui import (
    render_generation_ui
)

from style_intelligence.compliance_review_ui import (
    render_compliance_review
)

from style_intelligence.approved_document_ui import (
    render_approved_document
)

from publishing.publish_ui import (
    render_publishing_ui
)

from shared.export_center.export_center import (
    render_export_center
)

from shared.change_source_loader import (
    render_change_source_loader
)

from shared.work_item_service import (
    load_work_items
)

from generate_docs.template_selector_ui import (
    render_template_selector
)

from generate_docs.style_selector_ui import (
    render_style_selector
)


def render_generate_docs():

    st.title(
        "📝 Generate Documentation"
    )

    #
    # Change Source
    #

    change_source = (
        render_change_source_loader()
    )

    work_items = (
        load_work_items(
            change_source
        )
    )

    #
    # Document Type
    #

    document_type = st.selectbox(

        "Document Type",

        [
            "User Guide",
            "FAQ",
            "Release Notes",
            "Knowledge Base",
            "Quick Start Guide",
            "Video Script",
            "Solution Article",
            "API Guide"
        ]

    )

    #
    # Template
    #

    template_selection = (
        render_template_selector(
            document_type
        )
    )

    #
    # Style Guide
    #

    style_guide = (
        render_style_selector()
    )

    #
    # Generate Documentation
    #

    render_generation_ui(

        work_items,

        document_type,

        style_guide,

        template_selection

    )

    #
    # Get Generated Documents
    #

    generated_documents = (
        st.session_state.get(
            "generated_documents"
        )
    )

    if not generated_documents:

        return

    #
    # Generated Documentation
    #

    st.divider()

    st.header(
        "Generated Documentation"
    )

    #
    # Process Documents
    #

    for index, document in enumerate(
        generated_documents
    ):

        st.subheader(
            document["summary"]
        )

        st.markdown(
            document["document"]
        )

        #
        # Style Compliance
        #

        approved_document = (
            render_compliance_review(

                document,

                index,

                style_guide

            )
        )

        #
        # Approved Document
        #

        if approved_document:

            render_approved_document(

                approved_document,

                document["summary"]

            )

            #
            # Publishing
            #

            render_publishing_ui(

                document["summary"],

                approved_document["document"]

            )

        else:

            #
            # Original Document Export
            #

            render_export_center(

                title=document["summary"],

                content=document["document"]

            )