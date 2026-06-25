import streamlit as st

from utils.excel_exporter import (
    export_matched_articles
)


def render_discovery_results(
    matched_articles
):

    if not matched_articles:

        st.warning(
            "No impacted articles found."
        )

        return []

    st.subheader(
        "📄 Step 2: Review & Select Articles"
    )

    st.success(
        f"Articles Found: {len(matched_articles)}"
    )

    #
    # Export
    #

    excel = export_matched_articles(
        matched_articles
    )

    st.download_button(

        "⬇ Export Matched Articles",

        data=excel,

        file_name="matched_articles.xlsx",

        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "✅ Select All"
        ):

            st.session_state[
                "selected_articles"
            ] = [
                article["title"]
                for article in matched_articles
            ]

    with col2:

        if st.button(
            "❌ Clear Selection"
        ):

            st.session_state[
                "selected_articles"
            ] = []

    selected = []

    for article in matched_articles:

        confidence = article.get(
            "confidence",
            0
        )

        if confidence >= 90:

            badge = "🟢 High"

        elif confidence >= 70:

            badge = "🟡 Medium"

        else:

            badge = "🔴 Low"

        with st.container():

            checked = st.checkbox(

                article["title"],

                value=article["title"] in
                st.session_state.get(
                    "selected_articles",
                    []
                ),

                key=article["url"]

            )

            c1, c2 = st.columns([1, 3])

            with c1:

                st.markdown(
                    f"**{badge}**"
                )

                st.caption(
                    f"{confidence}%"
                )

            with c2:

                matched = article.get(
                    "matched_on",
                    []
                )

                if matched:

                    st.write(
                        "**Matched On:** "
                        + ", ".join(
                            matched
                        )
                    )

                if article.get(
                    "reason"
                ):

                    st.write(
                        "**Reason:** "
                        + article[
                            "reason"
                        ]
                    )

                if article.get(
                    "affected_section"
                ):

                    st.write(
                        "**Affected Section:** "
                        + article[
                            "affected_section"
                        ]
                    )

                st.markdown(
                    f"🔗 {article['url']}"
                )

            st.divider()

            if checked:

                selected.append(
                    article
                )

    st.info(
        f"Selected Articles: {len(selected)}"
    )

    return selected