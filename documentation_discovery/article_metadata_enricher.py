import requests

from bs4 import BeautifulSoup


def enrich_article(
    article
):
    """
    Enriches an inventory entry
    without downloading the
    entire article content.
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
        # Title
        #

        title = soup.title.get_text().strip() \
            if soup.title else article.get(
                "title",
                ""
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

        article["title"] = title

        article["description"] = description

        article["discovered_by"] = article.get(
            "discovered_by",
            "unknown"
        )

        article["content_fetched"] = False

        return article

    except Exception:

        return article