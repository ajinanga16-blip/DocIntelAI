import streamlit as st

from agents.article_metadata_extractor import (
    extract_article_metadata
)

import requests

from bs4 import BeautifulSoup


def show_page():

    st.title("🛠 Developer Tools")

    st.subheader(
        "Metadata Extractor Test"
    )

    url = st.text_input(
        "Documentation URL"
    )

    if st.button(
        "Run Metadata Extraction"
    ):

        if not url:

            st.warning(
                "Enter a URL."
            )

            return

        with st.spinner(
            "Downloading article..."
        ):

            response = requests.get(
                url,
                timeout=30
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            for tag in soup(
                [
                    "script",
                    "style",
                    "noscript"
                ]
            ):

                tag.decompose()

            title = (
                soup.title.get_text().strip()
                if soup.title
                else ""
            )

            content = soup.get_text(
                separator=" ",
                strip=True
            )

        st.success(
            f"Downloaded {len(content)} characters."
        )

        st.write(
            "Title:",
            title
        )

        metadata = extract_article_metadata(

            title=title,

            url=url,

            content=content

        )

        st.write(metadata)

        st.divider()

        st.subheader(
            "AI Metadata"
        )

        st.json(
            metadata
        )