import requests

from bs4 import BeautifulSoup

from agents.article_metadata_extractor import (
    extract_article_metadata
)


def enrich_article(
    article
):
    """
    Enrich repository article.

    Downloads the page,
    extracts visible content,
    generates AI metadata,
    then discards the content.
    """

    try:

        response = requests.get(
            article["url"],
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        #
        # Remove unwanted tags
        #

        for tag in soup([
            "script",
            "style",
            "noscript"
        ]):

            tag.decompose()

        #
        # Title
        #

        title = (
            soup.title.get_text().strip()
            if soup.title
            else article.get(
                "title",
                ""
            )
        )

        #
        # Description
        #

        description = ""

        meta = soup.find(
            "meta",
            attrs={
                "name": "description"
            }
        )

        if meta:

            description = meta.get(
                "content",
                ""
            )

        #
        # Visible Content
        #

        content = soup.get_text(
            separator=" ",
            strip=True
        )

        #
        # AI Metadata
        #

        metadata = extract_article_metadata(

            title=title,

            url=article["url"],

            content=content

        )

        #
        # Populate Article
        #

        article["title"] = title

        article["description"] = metadata.get(
            "description",
            description
        )

        article["category"] = metadata.get(
            "category",
            ""
        )

        article["features"] = metadata.get(
            "features",
            []
        )

        article["tasks"] = metadata.get(
            "tasks",
            []
        )

        article["keywords"] = metadata.get(
            "keywords",
            []
        )

        article["ui_elements"] = metadata.get(
            "ui_elements",
            []
        )

        article["error_topics"] = metadata.get(
            "error_topics",
            []
        )

        article["discovered_by"] = article.get(
            "discovered_by",
            "unknown"
        )

        article["content_fetched"] = False

        #
        # Do NOT save article content
        #

        return article

    except Exception as ex:

        print("=" * 60)
        print("ARTICLE ENRICHMENT FAILED")
        print(article.get("url"))
        print(type(ex).__name__)
        print(str(ex))
        print("Continuing with basic metadata...")
        print("=" * 60)

        #
        # Preserve repository build by returning
        # the article with minimal metadata.
        #

        article["description"] = article.get("description", "")
        article["category"] = article.get("category", "")
        article["features"] = article.get("features", [])
        article["tasks"] = article.get("tasks", [])
        article["keywords"] = article.get("keywords", [])
        article["ui_elements"] = article.get("ui_elements", [])
        article["error_topics"] = article.get("error_topics", [])

        article.pop("content", None)

        return article