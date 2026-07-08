from agents.site_crawler_agent import (
    crawl_site_links
)

links = crawl_site_links(
    "https://support.freshservice.com"
)

print(
    f"Links Found: {len(links)}"
)

for link in links[:20]:

    print(link)