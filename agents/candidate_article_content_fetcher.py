from agents.article_content_fetcher import (
    fetch_article_content
)


def fetch_candidate_content(
    matched_articles,
    max_articles=10
):

    content_articles = []

    for article in matched_articles[:max_articles]:

        try:

            content = fetch_article_content(
                article["url"]
            )

            if content:

                content_articles.append(
                    {
                        "title":
                            content["title"],

                        "url":
                            content["url"],

                        "content":
                            content["content"],

                        "confidence":
                            article.get(
                                "confidence",
                                0
                            ),

                        "reason":
                            article.get(
                                "reason",
                                ""
                            )
                    }
                )

        except Exception:

            continue

    return content_articles