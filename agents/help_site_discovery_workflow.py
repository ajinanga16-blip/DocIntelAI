from agents.article_inventory_builder import build_article_inventory
from agents.site_crawler_agent import (
    crawl_site_links
)

from agents.category_expander_agent import (
    expand_category
)

from agents.article_link_filter_agent import (
    filter_article_links
)

from agents.article_url_filter_agent import (
    filter_real_articles
)

from agents.article_inventory_agent import (
    save_inventory,
    load_inventory,
    inventory_exists
)


def discover_help_site_articles(
    help_site_url
):

    if inventory_exists():

        return load_inventory()

    links = crawl_site_links(
        help_site_url
    )

    expanded = []

    for link in links:

        expanded.extend(
            expand_category(
                link
            )
        )

    filtered = filter_article_links(
        expanded
    )

    from agents.article_inventory_builder import (
    build_article_inventory
    )

    ...

    articles = filter_real_articles(
        filtered
    )

    
    save_inventory(
        articles
    )

    return articles