import streamlit as st

from style_intelligence.document_compliance_service import (
    DocumentComplianceService
)

from style_intelligence.approved_document_builder import (
    ApprovedDocumentBuilder
)


def render_compliance_review(
    document,
    index,
    style_guide
):
    """
    Render Style Compliance and Human Review UI.
    """

    compliance_service = (
        DocumentComplianceService()
    )

    approved_builder = (
        ApprovedDocumentBuilder()
    )

    compliance_key = (
        f"compliance_{index}"
    )

    if st.button(
        "✅ Run Style Compliance",
        key=f"run_compliance_{index}",
        width="stretch"
    ):

        with st.spinner(
            "Running style compliance..."
        ):

            st.session_state[
                compliance_key
            ] = compliance_service.analyze(

                document["document"],

                style_guide

            )

    compliance_result = (
        st.session_state.get(
            compliance_key
        )
    )

    if not compliance_result:

        return None

    if compliance_result["violations"]:

        with st.expander(
            "View Violations"
        ):

            for violation in (
                compliance_result["violations"]
            ):

                st.markdown(
                    f"""
**Category:** {violation['category']}

**Rule:** {violation['rule']}

**Issue:** {violation['violation']}

**Suggestion:** {violation['suggestion']}

---
"""
                )

        st.subheader(
            "Review Suggestions"
        )

        for suggestion in (
            compliance_result["suggestions"]
        ):

            with st.container(
                border=True
            ):

                st.write(
                    f"**Category:** "
                    f"{suggestion['category']}"
                )

                st.write(
                    f"**Issue:** "
                    f"{suggestion['original']}"
                )

                st.write(
                    f"**Suggestion:** "
                    f"{suggestion['suggestion']}"
                )

                col1, col2 = (
                    st.columns(2)
                )

                with col1:

                    if st.button(
                        "🟢 Accept",
                        key=(
                            f"accept_"
                            f"{index}_"
                            f"{suggestion['id']}"
                        )
                    ):

                        suggestion[
                            "status"
                        ] = "Accepted"

                with col2:

                    if st.button(
                        "🟠 Reject",
                        key=(
                            f"reject_"
                            f"{index}_"
                            f"{suggestion['id']}"
                        )
                    ):

                        suggestion[
                            "status"
                        ] = "Rejected"

                st.caption(
                    f"Status: "
                    f"{suggestion['status']}"
                )

        st.divider()

        accepted = sum(

            1

            for suggestion in (
                compliance_result["suggestions"]
            )

            if suggestion["status"]
            == "Accepted"

        )

        rejected = sum(

            1

            for suggestion in (
                compliance_result["suggestions"]
            )

            if suggestion["status"]
            == "Rejected"

        )

        pending = sum(

            1

            for suggestion in (
                compliance_result["suggestions"]
            )

            if suggestion["status"]
            == "Pending"

        )

        col1, col2, col3 = (
            st.columns(3)
        )

        with col1:

            st.metric(
                "Accepted",
                accepted
            )

        with col2:

            st.metric(
                "Rejected",
                rejected
            )

        with col3:

            st.metric(
                "Pending",
                pending
            )

        col1, col2 = (
            st.columns(2)
        )

        with col1:

            if st.button(
                "🟢 Accept All",
                key=f"accept_all_{index}",
                width="stretch"
            ):

                for suggestion in (
                    compliance_result["suggestions"]
                ):

                    suggestion[
                        "status"
                    ] = "Accepted"

                st.rerun()

        with col2:

            if st.button(
                "🟠 Reject All",
                key=f"reject_all_{index}",
                width="stretch"
            ):

                for suggestion in (
                    compliance_result["suggestions"]
                ):

                    suggestion[
                        "status"
                    ] = "Rejected"

                st.rerun()

        st.metric(
            "Original Score",
            compliance_result["score"]
        )

        st.write(
            "Violations Found: "
            f"**{len(compliance_result['violations'])}**"
        )

        st.divider()

        if st.button(
            "🟢 Build Approved Document",
            key=f"build_document_{index}",
            width="stretch"
        ):

            approved_document = (
                approved_builder.build(
                    document["document"],
                    compliance_result[
                        "suggestions"
                    ]
                )
            )

            final_result = (
                compliance_service.analyze(
                    approved_document,
                    style_guide
                )
            )

            st.session_state[
                f"approved_document_{index}"
            ] = {

                "document":
                    approved_document,

                "score":
                    final_result["score"]

            }

    return st.session_state.get(
        f"approved_document_{index}"
    )