from agents.help_site_sitemap_agent import (
    get_sitemap_urls
)

urls = get_sitemap_urls(
    "https://support.freshservice.com"
)

print(
    f"Found {len(urls)} URLs"
)

for url in urls[:20]:

    print(url)