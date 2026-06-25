import requests

from urllib.parse import (
    urlparse,
    urljoin
)


COMMON_SITEMAPS = [

    "/sitemap.xml",

    "/sitemap_index.xml",

    "/sitemap-index.xml",

    "/support/sitemap.xml",

    "/docs/sitemap.xml"

]


def discover_site(
    documentation_url
):
    """
    Determines the best discovery
    strategy for a documentation site.
    """

    parsed = urlparse(
        documentation_url
    )

    base_url = (
        f"{parsed.scheme}://{parsed.netloc}"
    )

    #
    # Step 1
    # robots.txt
    #

    robots_url = urljoin(
        base_url,
        "/robots.txt"
    )

    try:

        response = requests.get(
            robots_url,
            timeout=10
        )

        if response.ok:

            for line in response.text.splitlines():

                if line.lower().startswith(
                    "sitemap:"
                ):

                    sitemap = line.split(
                        ":",
                        1
                    )[1].strip()

                    return {

                        "strategy":
                            "sitemap",

                        "sitemap":
                            sitemap

                    }

    except Exception:

        pass

    #
    # Step 2
    # Common sitemap locations
    #

    for location in COMMON_SITEMAPS:

        sitemap = urljoin(
            base_url,
            location
        )

        try:

            response = requests.get(
                sitemap,
                timeout=10
            )

            if response.ok:

                return {

                    "strategy":
                        "sitemap",

                    "sitemap":
                        sitemap

                }

        except Exception:

            pass

    #
    # Step 3
    #

    return {

        "strategy":
            "crawl"

    }