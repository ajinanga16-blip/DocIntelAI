import streamlit as st

from publishing.publish_service import (
    PublishService
)

from publishing.publish_result import (
    PublishRequest
)


def render_publishing_ui(
    document_title,
    document_content
):
    """
    Render publishing configuration and
    execute publishing for the supplied document.
    """

    st.divider()

    st.subheader(
        "🚀 Publish"
    )

    destination = st.selectbox(

        "Publish Destination",

        [
            "Local Folder",
            "GitHub Repository",
            "GitHub Pages",
            "MkDocs",
            "Docusaurus",
            "Confluence"
        ],

        key=f"publish_destination_{document_title}"

    )

    config = {}

    if destination == "Local Folder":

        config["output_folder"] = (
            st.text_input(
                "Output Folder",
                key=f"publish_folder_{document_title}"
            )
        )

    elif destination in (
        "MkDocs",
        "Docusaurus"
    ):

        config["output_folder"] = (
            st.text_input(
                "Project Folder",
                key=f"publish_project_folder_{document_title}"
            )
        )

    elif destination in (
        "GitHub Repository",
        "GitHub Pages"
    ):

        config["repository"] = (
            st.text_input(
                "Repository",
                key=f"publish_repository_{document_title}"
            )
        )

        config["github_token"] = (
            st.text_input(
                "GitHub Personal Access Token",
                type="password",
                key=f"publish_github_token_{document_title}"
            )
        )

        config["branch"] = (
            st.text_input(
                "Branch",
                value="main",
                key=f"publish_branch_{document_title}"
            )
        )

    elif destination == "Confluence":

        config["base_url"] = (
            st.text_input(
                "Confluence URL",
                key=f"publish_confluence_url_{document_title}"
            )
        )

        config["email"] = (
            st.text_input(
                "Email",
                key=f"publish_confluence_email_{document_title}"
            )
        )

        config["api_token"] = (
            st.text_input(
                "API Token",
                type="password",
                key=f"publish_confluence_token_{document_title}"
            )
        )

        config["space_key"] = (
            st.text_input(
                "Space Key",
                key=f"publish_confluence_space_{document_title}"
            )
        )

        config["parent_id"] = (
            st.text_input(
                "Parent Page ID (Optional)",
                key=f"publish_confluence_parent_{document_title}"
            )
        )

    publish = st.button(
        "🚀 Publish",
        width="stretch",
        key=f"publish_button_{document_title}"
    )

    if not publish:

        return

    publish_service = (
        PublishService()
    )

    request = PublishRequest(

        destination=destination,

        title=document_title,

        content=document_content,

        output_folder=config.get(
            "output_folder"
        ),

        repository=config.get(
            "repository"
        ),

        branch=config.get(
            "branch"
        ),

        github_token=config.get(
            "github_token"
        ),

        base_url=config.get(
            "base_url"
        ),

        email=config.get(
            "email"
        ),

        api_token=config.get(
            "api_token"
        ),

        space_key=config.get(
            "space_key"
        ),

        parent_id=config.get(
            "parent_id"
        )

    )

    result = (
        publish_service.publish(
            request
        )
    )

    if result["success"]:

        st.success(
            result["message"]
        )

        if result.get("location"):

            st.info(
                f"Location: {result['location']}"
            )

        if result.get("url"):

            st.success(
                f"Published URL: {result['url']}"
            )

    else:

        st.error(
            result["message"]
        )