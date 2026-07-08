from agents.article_clustering_agent import (
    cluster_articles
)

sample_articles = [
    {
        "title": "Assign User Role",
        "url": "url1"
    },
    {
        "title": "Create User",
        "url": "url2"
    },
    {
        "title": "User Role FAQ",
        "url": "url3"
    },
    {
        "title": "Configure SSO",
        "url": "url4"
    }
]

result = cluster_articles(
    sample_articles
)

print(result)