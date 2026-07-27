import streamlit as st

from shared.export_center.export_center import (
    render_export_center
)

from documentation_actions.documentation_generation_mapper import (
    action_plan_to_requirements
)

from agents.documentation_agent import (
    generate_documentation_from_requirements
)


def render_action_plan(results):

    st.divider()

    st.subheader(
        "Documentation Action Plan"
    )

    document_type = st.selectbox(
        "Document Type",
        [
            "User Guide",
            "FAQ",
            "Release Notes",
            "Knowledge Base",
            "Solution Article"
        ]
    )


    style_guide = st.selectbox(
        "Style Guide",
        [
            "Microsoft",
            "Google",
            "IBM"
        ]
    )

    for result in results:

        work_item = result["work_item"]

        with st.container(border=True):

            st.markdown(
                f"## {work_item.get('ticket_id','')} - "
                f"{work_item.get('summary','')}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Overall Action",
                    result["overall_action"]
                )

            with col2:

                st.metric(
                    "Estimated Effort",
                    result["estimated_effort"]
                )

            st.markdown(
                "### Impacted Documentation"
            )

            impacted_articles = result.get(
                "impacted_articles",
                []
            )

            if not impacted_articles:

                st.info(
                    "No existing documentation found."
                )

            else:

                for article_index, article in enumerate(
                    impacted_articles
                ):

                    col1, col2 = st.columns([1, 8])

                    with col1:
                        article["generate"] = st.checkbox(
                            "Generate",
                            key=f"{work_item.get('ticket_id')}_{article_index}",
                            label_visibility="collapsed"
                        )

                    with col2:

                        title = article.get("title", "")
                        url = article.get("url", "")

                        if url:
                            st.markdown(f"[{title}]({url})")
                        else:
                            st.write(title)

                    col1, col2 = st.columns([1, 3])

                    # with col1:
                    #
                    #    st.write("Coverage")
                    #
                    # with col2:
                    #
                    #    st.write(
                    #        article.get(
                    #            "coverage",
                    #            ""
                    #        )
                    #    )

                    st.write(
                        "Required Change"
                    )

                    st.info(
                        article.get(
                            "required_change",
                            ""
                        )
                    )

                    gap = article.get(
                        "gap",
                        ""
                    )

                    if gap:

                        st.caption(
                            f"Gap: {gap}"
                        )

            if st.button(
                "📄 Generate Selected Documentation",
                key=f"generate_{work_item.get('ticket_id')}"
            ):

                structured_requirements = action_plan_to_requirements(
                    result
                )

                generated_document = (
                    generate_documentation_from_requirements(
                        structured_requirements=structured_requirements,
                        document_type=document_type,
                        style_guide=style_guide,
                        template_source="Built-in",
                        template_name=None
                    )
                )

                st.success(
                    "Documentation generated successfully."
                )

                st.divider()

                st.subheader(
                    "📄 Generated Documentation"
                )

                st.markdown(
                    generated_document
                )

                render_export_center(
                    f"{work_item.get('ticket_id')}_Documentation",
                    generated_document
                )