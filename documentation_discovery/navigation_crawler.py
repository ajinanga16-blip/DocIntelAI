import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)

from collections import deque


def crawl_documentation(
    start_url,
    max_pages=1000
):

    visited = set()

    queue = deque([start_url])

    articles = []

    domain = urlparse(
        start_url
    ).netloc

    while queue:

        current = queue.popleft()

        if current in visited:

            continue

        visited.add(current)

        if len(visited) >= max_pages:

            break

        try:

            response = requests.get(
                current,
                timeout=20
            )

            response.raise_for_status()

        except Exception:

            continue

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup.find_all(
            "a",
            href=True
        ):

            href = urljoin(
                current,
                tag["href"]
            )

            if urlparse(
                href
            ).netloc != domain:

                continue

            title = tag.get_text().strip()

            if "/article" in href or "/articles/" in href:

                articles.append({

                    "title": title,

                    "url": href,

                    "discovered_by": "navigation"

                })

            elif href not in visited:

                queue.append(
                    href
                )

    dedup = {}

    for article in articles:

        dedup[
            article["url"]
        ] = article

    return list(
        dedup.values()
    )