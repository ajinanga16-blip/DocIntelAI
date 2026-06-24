import streamlit as st


def render_compliance_results(
    compliance
):

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
            "No style violations found."
        )