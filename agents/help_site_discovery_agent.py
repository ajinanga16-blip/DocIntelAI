from agents.documentation_url_fetcher import (
    fetch_documentation_content
)


def discover_candidate_articles(
    help_site_url,
    queries
):

    candidates = []

    try:

        content = fetch_documentation_content(
            help_site_url
        )

        candidates.append(
            {
                "title": "Help Site Root",
                "url": help_site_url,
                "content": content
            }
        )

    except Exception:

        pass

    return candidates