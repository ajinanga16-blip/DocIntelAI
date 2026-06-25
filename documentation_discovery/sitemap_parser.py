import requests
import xml.etree.ElementTree as ET


NAMESPACE = {
    "sm": "http://www.sitemaps.org/schemas/sitemap/0.9"
}


def parse_sitemap(
    sitemap_url
):
    """
    Supports both:

    • sitemap.xml

    • sitemap_index.xml
    """

    urls = []

    _parse(
        sitemap_url,
        urls
    )

    dedup = {}

    for article in urls:

        dedup[
            article["url"]
        ] = article

    return list(
        dedup.values()
    )


def _parse(
    sitemap_url,
    urls
):

    response = requests.get(
        sitemap_url,
        timeout=30
    )

    response.raise_for_status()

    root = ET.fromstring(
        response.content
    )

    #
    # Sitemap Index
    #

    if root.tag.endswith(
        "sitemapindex"
    ):

        for sitemap in root.findall(
            "sm:sitemap",
            NAMESPACE
        ):

            loc = sitemap.find(
                "sm:loc",
                NAMESPACE
            )

            if loc is not None:

                _parse(
                    loc.text.strip(),
                    urls
                )

        return

    #
    # Standard Sitemap
    #

    for url in root.findall(
        "sm:url",
        NAMESPACE
    ):

        loc = url.find(
            "sm:loc",
            NAMESPACE
        )

        if loc is None:

            continue

        urls.append(

            {
                "title": "",
                "url": loc.text.strip()
            }

        )