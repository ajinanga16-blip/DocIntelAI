import streamlit as st

from agents.content_agent import (
    generate_documentation
)

from agents.jira_agent import (
    fetch_jira_ticket
)

from agents.jira_intelligence_agent import (
    build_structured_requirements
)

from agents.documentation_agent import (
    generate_documentation_from_requirements
)

from style_intelligence.document_compliance_service import (
    DocumentComplianceService
)

from style_intelligence.style_selector import (
    StyleSelector
)


def render_generate_docs():

    st.title(
        "📝 Generate Documentation"
    )

    source_type = st.radio(
        "Source Type",
        [
            "Manual Input",
            "JIRA Ticket"
        ]
    )

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

    selector = StyleSelector()

    builtin_styles = (
        selector.get_builtin_styles()
    )

    custom_styles = (
        selector.get_custom_styles()
    )

    style_source = st.radio(
        "Style Source",
        [
            "Built-in",
            "Custom"
        ]
    )

    if style_source == "Built-in":

        style_guide = st.selectbox(
            "Built-in Style Guide",
            builtin_styles
        )

    else:

        if not custom_styles:

            st.warning(
                "No custom style guides available."
            )

            style_guide = None

        else:

            style_guide = st.selectbox(
                "Custom Style Guide",
                custom_styles
            )

    # ----------------------------------
    # Manual Input
    # ----------------------------------

    if source_type == "Manual Input":

        feature_description = st.text_area(
            "Feature Description",
            height=200
        )

        if st.button(
            "Generate Documentation"
        ):

            with st.spinner(
                "Generating documentation..."
            ):

                result = (
                    generate_documentation(
                        feature_description,
                        document_type
                    )
                )

            st.success(
                "Documentation generated successfully."
            )

            st.markdown(result)

    # ----------------------------------
    # JIRA Ticket
    # ----------------------------------

    else:

        ticket_id = st.text_input(
            "JIRA Ticket ID",
            placeholder="SCRUM-5"
        )

        if st.button(
            "Generate From JIRA"
        ):

            if not ticket_id:

                st.error(
                    "Please enter a JIRA Ticket ID."
                )

            else:

                try:

                    with st.spinner(
                        "Fetching JIRA ticket..."
                    ):

                        ticket_data = (
                            fetch_jira_ticket(
                                ticket_id
                            )
                        )

                    with st.spinner(
                        "Analyzing requirements..."
                    ):

                        structured_requirements = (
                            build_structured_requirements(
                                ticket_data
                            )
                        )

                    with st.spinner(
                        "Generating documentation..."
                    ):

                        result = (
                            generate_documentation_from_requirements(
                                structured_requirements,
                                document_type,
                                style_guide
                            )
                        )

                    st.success(
                        "Documentation generated successfully."
                    )

                    st.subheader(
                        "Generated Document"
                    )

                    st.markdown(result)

                    compliance_service = (
                        DocumentComplianceService()
                    )

                    compliance = (
                        compliance_service.analyze(
                            result,
                            style_guide
                        )
                    )

                    st.divider()

                    st.subheader(
                        "Style Compliance Analysis"
                    )

                    st.metric(
                        "Original Score",
                        compliance["score"]
                    )

                    violations = (
                        compliance["violations"]
                    )

                    st.write(
                        f"Violations Found: {len(violations)}"
                    )

                    for violation in violations:

                        with st.expander(
                            violation["category"]
                        ):

                            st.write(
                                f"Rule: {violation['rule']}"
                            )

                            st.write(
                                f"Issue: {violation['violation']}"
                            )

                            st.write(
                                f"Suggestion: {violation['suggestion']}"
                            )

                            st.write(
                                f"Severity: {violation['severity']}"
                            )

                    st.divider()

                    if "corrected_document" in compliance:

                        st.divider()

                        st.subheader(
                             "Corrected Document"
                        )

                        st.markdown(
                             compliance[
                                 "corrected_document"
                            ]
                        )

                        st.metric(
                             "Corrected Score",
                            compliance[
                                 "corrected_score"
                            ]
                        )

                    else:

                        st.success(
                            "No style violations found. No corrections required."
                        )
                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )