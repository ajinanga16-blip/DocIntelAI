import streamlit as st


from pages.job_result_page import (
    show_page as show_job_result
)

from pages.ux_intelligence_page import (
    show_page as show_ux_intelligence
)

from pages.developer_tools_page import (
    show_page as show_developer_tools
)

from pages.notification_page import (
    show_page as show_notifications
)

from pages.job_manager_page import (
    show_page as show_job_manager
)

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
    show_page as show_gap_analysis
)

from pages.generate_docs_page import (
    render_generate_docs
)

from pages.dashboard_page import (
    render_dashboard
)

from pages.screenshot_intelligence_page import (
    show_page as show_screenshot_intelligence
)


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


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="DocIntel AI",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# Application Branding
# --------------------------------------------------

#st.sidebar.title(
#    #"📚 DocIntel AI"
#)


# --------------------------------------------------
# Application Navigation
# --------------------------------------------------

dashboard_page = st.Page(

    render_dashboard,

    title="Dashboard",

    icon="🏠",

    url_path="dashboard",

    default=True

)


generate_docs_page = st.Page(

    render_generate_docs,

    title="Create Docs",

    icon="📄",

    url_path="create-docs"

)


styles_templates_page = st.Page(

    render_template_management,

    title="Styles & Templates Management",

    icon="🎨",

    url_path="styles-templates"

)


screenshot_intelligence_page = st.Page(

    show_screenshot_intelligence,

    title="Screenshot Intelligence",

    icon="🖼️",

    url_path="screenshot-intelligence"

)


ux_intelligence_page = st.Page(

    show_ux_intelligence,

    title="UX Intelligence",

    icon="✍️",

    url_path="ux-intelligence"

)


connect_documentation_page = st.Page(

    show_inventory_builder,

    title="Connect Documentation",

    icon="🔗",

    url_path="connect-documentation"

)


repository_dashboard_page = st.Page(

    show_repository_dashboard,

    title="Repository Dashboard",

    icon="🗂️",

    url_path="repository-dashboard"

)


job_manager_page = st.Page(

    show_job_manager,

    title="Job Manager",

    icon="⚙️",

    url_path="job-manager"

)


notifications_page = st.Page(

    show_notifications,

    title="Notifications",

    icon="🔔",

    url_path="notifications"

)


gap_analysis_page = st.Page(

    show_gap_analysis,

    title="Gap Analysis",

    icon="🔎",

    url_path="gap-analysis"

)


impact_analysis_page = st.Page(

    render_impact_analysis,

    title="Impact Analysis",

    icon="📊",

    url_path="impact-analysis"

)


# --------------------------------------------------
# Visible Application Navigation
# --------------------------------------------------
#
# IMPORTANT:
#
# Only pages listed here are exposed in the
# Streamlit navigation.
#
# The other files inside /pages are intentionally
# left in the project but are NOT exposed here.
#
# --------------------------------------------------

pg = st.navigation(

    [

        dashboard_page,

        generate_docs_page,

        styles_templates_page,

        screenshot_intelligence_page,

        ux_intelligence_page,

        connect_documentation_page,

        repository_dashboard_page,

        job_manager_page,

        notifications_page,

        gap_analysis_page,

        impact_analysis_page

    ],

    position="sidebar"

)


# --------------------------------------------------
# Run Selected Page
# --------------------------------------------------

pg.run()