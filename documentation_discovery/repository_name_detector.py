import requests

from bs4 import BeautifulSoup

from urllib.parse import urlparse


def detect_repository_name(
    documentation_url
):
    """
    Attempts to determine a friendly
    repository name from the site.
    """

    try:

        response = requests.get(
            documentation_url,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        #
        # Open Graph
        #

        tag = soup.find(
            "meta",
            property="og:site_name"
        )

        if tag and tag.get("content"):

            return tag["content"].strip()

        #
        # HTML Title
        #

        if soup.title:

            title = soup.title.get_text().strip()

            if "|" in title:

                return title.split("|")[0].strip()

            if "-" in title:

                return title.split("-")[0].strip()

            return title

    except Exception:

        pass

    #
    # Fallback
    #

    domain = urlparse(
        documentation_url
    ).netloc

    domain = domain.replace(
        "www.",
        ""
    )

    return domain