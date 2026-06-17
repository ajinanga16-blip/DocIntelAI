from pages.gap_analysis_page import (
    render_gap_analysis
)
from pages.generate_docs_page import (
    render_generate_docs
)
from pages.dashboard_page import (
    render_dashboard
)
from agents.content_agent import generate_documentation

from agents.jira_agent import fetch_jira_ticket

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

import streamlit as st


st.set_page_config(
    page_title="DocIntel AI",
    page_icon="📚",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📚 DocIntel AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Generate Docs",
        "Gap Analysis",
        "Impact Analysis",
        "Publishing",
        "Settings"
    ]
)

# --------------------------------------------------
# Dashboard
# --------------------------------------------------

if page == "Dashboard":

    render_dashboard()

# --------------------------------------------------
# Generate Docs
# --------------------------------------------------

elif page == "Generate Docs":

    render_generate_docs()

# --------------------------------------------------
# Gap Analysis
# --------------------------------------------------

elif page == "Gap Analysis":

    render_gap_analysis()
# --------------------------------------------------
# Impact Analysis
# --------------------------------------------------

elif page == "Impact Analysis":

    st.title(
        "⚡ Impact Analysis"
    )

    st.text_input(
        "Release or Ticket ID"
    )

    st.button(
        "Run Impact Analysis"
    )

# --------------------------------------------------
# Publishing
# --------------------------------------------------

elif page == "Publishing":

    st.title(
        "🚀 Publishing"
    )

    st.selectbox(
        "Publish Destination",
        [
            "MkDocs",
            "GitHub Pages",
            "Confluence"
        ]
    )

    st.button(
        "Publish"
    )

# --------------------------------------------------
# Settings
# --------------------------------------------------

elif page == "Settings":

    st.title(
        "⚙ Settings"
    )

    st.write(
        "Configure integrations here."
    )