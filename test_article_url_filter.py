from agents.category_expander_agent import (
    expand_category
)

from agents.article_link_filter_agent import (
    filter_article_links
)

from agents.article_url_filter_agent import (
    filter_real_articles
)

links = expand_category(
    "https://support.freshservice.com/support/solutions/50000000126"
)

filtered = filter_article_links(
    links
)

articles = filter_real_articles(
    filtered
)

print(
    f"Articles Found: {len(articles)}"
)

for item in articles[:20]:

    print(item["title"])
    print(item["url"])
    print("---")