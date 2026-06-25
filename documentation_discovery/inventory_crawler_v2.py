import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)

from collections import deque


def crawl_help_site_v2(
    start_url,
    max_pages=1000
):
    """
    Breadth-first crawler for documentation sites.

    Discovers:
    - Categories
    - Subcategories
    - Articles

    Prevents revisiting URLs.
    """

    visited = set()

    queue = deque()

    queue.append(
        (
            start_url,
            0
        )
    )

    articles = []

    domain = urlparse(
        start_url
    ).netloc

    while queue:

        current_url, depth = queue.popleft()

        if current_url in visited:
            continue

        visited.add(
            current_url
        )

        if len(visited) >= max_pages:
            break

        try:

            response = requests.get(
                current_url,
                timeout=20
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

        except Exception:

            continue

        #
        # Discover links
        #

        for tag in soup.find_all(
            "a",
            href=True
        ):

            href = urljoin(
                current_url,
                tag["href"]
            )

            if urlparse(
                href
            ).netloc != domain:

                continue

            title = (
                tag.get_text()
                .strip()
            )

            #
            # Article
            #

            if "/solutions/articles/" in href:

                articles.append(

                    {
                        "title": title,
                        "url": href,
                        "source_page": current_url,
                        "depth": depth
                    }

                )

            #
            # Continue crawling
            #

            elif (
                "/support/" in href
                and
                href not in visited
            ):

                queue.append(

                    (
                        href,
                        depth + 1
                    )

                )

    #
    # Remove duplicates
    #

    dedup = {}

    for article in articles:

        dedup[
            article["url"]
        ] = article

    return list(
        dedup.values()
    )