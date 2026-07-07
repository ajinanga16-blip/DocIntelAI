import streamlit as st


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

            st.button(

                "Generate Selected Documentation",

                key=f"generate_{work_item.get('ticket_id')}"

            )