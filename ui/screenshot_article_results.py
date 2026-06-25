import streamlit as st


def render_article_results(
    matched_articles
):

    if not matched_articles:

        st.info(
            "No impacted articles found."
        )

        return

    st.subheader(
        "Impacted Articles"
    )

    for article in matched_articles:

        with st.expander(
            article.get(
                "title",
                "Untitled"
            )
        ):

            st.write(
                f"**Confidence:** "
                f"{article.get('confidence', 0)}%"
            )

            if article.get(
                "affected_section"
            ):

                st.write(
                    f"**Affected Section:** "
                    f"{article['affected_section']}"
                )

            st.write(
                f"**Reason:** "
                f"{article.get('reason', '')}"
            )

            st.write(
                f"**URL:** "
                f"{article.get('url', '')}"
            )