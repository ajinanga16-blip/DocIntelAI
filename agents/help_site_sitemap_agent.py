import requests

from bs4 import BeautifulSoup


def get_sitemap_urls(
    help_site_url
):

    sitemap_urls = [
        f"{help_site_url.rstrip('/')}/sitemap.xml",
        f"{help_site_url.rstrip('/')}/sitemap-index.xml"
    ]

    for sitemap_url in sitemap_urls:

        try:

            response = requests.get(
                sitemap_url,
                timeout=20
            )

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(
                response.content,
                "xml"
            )

            urls = []

            for loc in soup.find_all("loc"):

                urls.append(
                    loc.text.strip()
                )

            if urls:

                return urls

        except Exception:

            continue

    return []