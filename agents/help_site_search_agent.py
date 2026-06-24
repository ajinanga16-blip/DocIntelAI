from config.search_config import (
    SEARCH_PROVIDER
)

from search.provider_factory import (
    get_search_provider
)

from agents.search_query_agent import (
    generate_search_queries
)


def find_relevant_articles(
    screenshot_file,
    help_site_url
):

    queries_text = (
        generate_search_queries(
            screenshot_file
        )
    )

    queries = [
        line.strip()
        for line in queries_text.splitlines()
        if line.strip()
    ]

    provider = (
        get_search_provider(
            SEARCH_PROVIDER
        )
    )

    all_results = []

    for query in queries:

        try:

            results = provider(
                query,
                help_site_url
            )

            all_results.extend(
                results
            )

        except Exception:

            pass

    unique_results = {}

    for result in all_results:

        unique_results[
            result["url"]
        ] = result

    return list(
        unique_results.values()
    )