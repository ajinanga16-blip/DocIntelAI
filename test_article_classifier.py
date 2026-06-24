from agents.article_classifier_agent import (
    classify_links
)

links = [
    "https://support.freshservice.com/support/home",
    "https://support.freshservice.com/support/solutions/50000000126",
    "https://www.freshworks.com/freshservice/",
    "https://community.freshworks.com/product-updates"
]

result = classify_links(
    links
)

print(result)