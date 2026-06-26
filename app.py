from pages.repository_dashboard_page import (
    show_page as show_repository_dashboard
)
from pages.inventory_builder_page import (
    show_page as show_inventory_builder
)
from pages.template_management_page import (
    render_template_management
)
from pages.settings_page import (
    render_settings
)
from pages.publishing_page import (
    render_publishing
)
from pages.impact_analysis_page import (
    render_impact_analysis
)
from pages.gap_analysis_page import (
    render_gap_analysis
)
from pages.generate_docs_page import (
    render_generate_docs
)
from pages.dashboard_page import (
    render_dashboard
)
from pages.screenshot_intelligence_page import (
    show_page
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
        "Template Management",
        "Screenshot Intelligence",
        "🔗 Connect Documentation",
        "🗂 Repository Dashboard",
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

    render_impact_analysis()

# --------------------------------------------------
# Publishing
# --------------------------------------------------

elif page == "Publishing":

    render_publishing()

# --------------------------------------------------
# Settings
# --------------------------------------------------

elif page == "Settings":

    render_settings()

# --------------------------------------------------
# Template Management
# --------------------------------------------------
elif page == "Template Management":

    render_template_management()

# --------------------------------------------------
# Screenshot Intelligence
# --------------------------------------------------

elif page == "Screenshot Intelligence":

    show_page()

# --------------------------------------------------
# Documentation Inventory
# --------------------------------------------------

elif page == "🔗 Connect Documentation":

    show_inventory_builder()

# --------------------------------------------------
# Repository Dashboard
# --------------------------------------------------

elif page == "🗂 Repository Dashboard":

    show_repository_dashboard()