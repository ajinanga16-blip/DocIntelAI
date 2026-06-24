import streamlit as st

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

from generate_docs.compliance_results import (
    render_compliance_results
)


def render_jira_generation(
    document_type,
    style_guide,
    template_selection
):

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

            return

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
                        style_guide,
                        template_selection["source"],
                        template_selection["template"]
                    )
                )

            st.success(
                "Documentation generated successfully."
            )

            st.subheader(
                "Generated Document"
            )

            st.markdown(
                result
            )

            compliance_service = (
                DocumentComplianceService()
            )

            compliance = (
                compliance_service.analyze(
                    result,
                    style_guide
                )
            )

            render_compliance_results(
                compliance
            )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )