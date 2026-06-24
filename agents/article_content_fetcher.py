import requests

from bs4 import BeautifulSoup


def fetch_article_content(
    article_url
):

    try:

        response = requests.get(
            article_url,
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = ""

        if soup.title:

            title = (
                soup.title.text.strip()
            )

        content = soup.get_text(
            separator=" ",
            strip=True
        )

        return {
            "title": title,
            "url": article_url,
            "content": content[:20000]
        }

    except Exception:

        return None