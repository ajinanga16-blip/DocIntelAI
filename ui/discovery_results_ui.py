import streamlit as st


def render_discovery_results(
    matched_articles
):
    """
    Displays impacted articles and
    allows the writer to select the
    ones they want to analyze further.
    """

    if not matched_articles:

        st.info(
            "No impacted articles found."
        )
        return []

    st.subheader(
        "Step 2: Review & Select Articles"
    )

    if st.button(
        "Select All"
    ):
        st.session_state[
            "selected_articles"
        ] = [
            article["title"]
            for article in matched_articles
        ]

    if st.button(
        "Clear Selection"
    ):
        st.session_state[
            "selected_articles"
        ] = []

    selected = []

    for article in matched_articles:

        checked = st.checkbox(

            f"{article['title']} "
            f"({article['confidence']}%)",

            value=article["title"] in
            st.session_state.get(
                "selected_articles",
                []
            ),

            key=article["url"]
        )

        st.caption(
            article.get(
                "reason",
                ""
            )
        )

        if article.get(
            "affected_section"
        ):

            st.caption(
                "Affected Section: "
                + article[
                    "affected_section"
                ]
            )

        st.divider()

        if checked:

            selected.append(
                article
            )

    return selected