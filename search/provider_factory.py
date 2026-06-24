from search.serper_provider import (
    search as serper_search
)

from search.tavily_provider import (
    search as tavily_search
)


def get_search_provider(
    provider_name
):

    if provider_name == "serper":

        return serper_search

    if provider_name == "tavily":

        return tavily_search

    raise ValueError(
        f"Unsupported provider: "
        f"{provider_name}"
    )