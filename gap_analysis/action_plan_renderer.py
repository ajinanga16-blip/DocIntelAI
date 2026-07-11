import streamlit as st

from shared.export_center.export_center import (
    render_export_center
)

def render_action_plan(results):

    st.divider()

    st.subheader(
        "Documentation Action Plan"
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

                    article["generate"] = st.checkbox(

                        article.get(
                            "title",
                            ""
                        ),

                        key=f"{work_item.get('ticket_id')}_{article_index}"

                    )

                    col1, col2 = st.columns([1, 3])

                    with col1:

                        st.write("Coverage")

                    with col2:

                        st.write(

                            article.get(

                                "coverage",

                                ""

                            )

                        )

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

                export_text = f"""
            Work Item:
            {work_item.get('ticket_id')}

            Summary:
            {work_item.get('summary')}

            Overall Action:
            {result['overall_action']}

            Estimated Effort:
            {result['estimated_effort']}
            """

                for article in impacted_articles:

                    if article.get("generate"):

                        export_text += f"""

            Article:
            {article.get('title')}

            Coverage:
            {article.get('coverage')}

            Required Change:
            {article.get('required_change')}

            Gap:
            {article.get('gap')}
            """

                st.success(
                    "Documentation package prepared."
                )

                st.divider()

                st.subheader("📄 Documentation Preview")

                st.text_area(

                    "Generated Documentation",

                    value=export_text,

                    height=350,

                    disabled=True

                )

                render_export_center(

                    f"{work_item.get('ticket_id')}_Action_Plan",

                    export_text

                )