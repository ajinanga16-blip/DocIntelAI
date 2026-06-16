import streamlit as st


def render_dashboard():

    st.title("📚 Dashboard")

    st.success(
        "Welcome to DocIntel AI"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Generated Articles",
            "124"
        )

    with col2:

        st.metric(
            "Documentation Gaps Found",
            "18"
        )