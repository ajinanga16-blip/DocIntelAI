import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin
)


def expand_category(
    category_url
):

    try:

        response = requests.get(
            category_url,
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        article_links = []

        for tag in soup.find_all(
            "a",
            href=True
        ):

            href = tag["href"]

            text = (
                tag.get_text()
                .strip()
            )

            if not text:

                continue

            from urllib.parse import (
                urljoin
            )

            ...

            if href:

             href = urljoin(
                category_url,
                href
            )

            if href.startswith(
                "http"
            ):

                article_links.append(
                    {
                        "title": text,
                        "url": href
                    }
                )

        return article_links

    except Exception:

        return []