import requests

from bs4 import BeautifulSoup


def crawl_site_links(
    site_url,
    max_links=100
):

    try:

        response = requests.get(
            site_url,
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        links = []

        for tag in soup.find_all(
            "a",
            href=True
        ):

            href = tag["href"]

            if href.startswith("/"):

                href = (
                    site_url.rstrip("/")
                    + href
                )

            if href.startswith(
                "http"
            ):

                links.append(
                    href
                )

        links = list(
            set(links)
        )

        return links[:max_links]

    except Exception:

        return []