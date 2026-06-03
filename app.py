from agents.content_agent import generate_documentation
import streamlit as st

st.set_page_config(
    page_title="DocIntel AI",
    page_icon="📚",
    layout="wide"
)

# Sidebar
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

# Dashboard
if page == "Dashboard":

    st.title("📚 Dashboard")

    st.success("Welcome to DocIntel AI")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Generated Articles", "124")

    with col2:
        st.metric("Documentation Gaps Found", "18")

# Generate Docs
elif page == "Generate Docs":

    st.title("📝 Generate Documentation")

    feature_description = st.text_area(
        "Feature Description",
        height=200
    )

    document_type = st.selectbox(
        "Document Type",
        [
            "User Guide",
            "FAQ",
            "Release Notes",
            "Knowledge Base"
        ]
    )

    if st.button("Generate"):

        with st.spinner("Generating documentation..."):

            result = generate_documentation(
                feature_description,
                document_type
            )

            st.markdown(result)
# Gap Analysis
elif page == "Gap Analysis":

    st.title("🔍 Knowledge Gap Analysis")

    st.file_uploader(
        "Upload Support Ticket CSV"
    )

    st.button("Analyze")

# Impact Analysis
elif page == "Impact Analysis":

    st.title("⚡ Impact Analysis")

    st.text_input("Release or Ticket ID")

    st.button("Run Impact Analysis")

# Publishing
elif page == "Publishing":

    st.title("🚀 Publishing")

    st.selectbox(
        "Publish Destination",
        [
            "MkDocs",
            "GitHub Pages",
            "Confluence"
        ]
    )

    st.button("Publish")

# Settings
elif page == "Settings":

    st.title("⚙ Settings")

    st.write("Configure integrations here.")