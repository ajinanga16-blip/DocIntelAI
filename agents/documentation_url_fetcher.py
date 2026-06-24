import requests

from bs4 import BeautifulSoup


def fetch_documentation_content(
    url
):

    response = requests.get(
        url,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for tag in soup(
        [
            "script",
            "style",
            "nav",
            "footer",
            "header"
        ]
    ):
        tag.decompose()

    text = soup.get_text(
        separator="\n"
    )

    cleaned_text = "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )

    return cleaned_text[:15000]