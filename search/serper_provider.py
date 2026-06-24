import os
import requests

from dotenv import load_dotenv

load_dotenv()


def search(
    query,
    site_url,
    num_results=10
):

    api_key = os.getenv(
        "SERPER_API_KEY"
    )

    search_query = (
        f"site:{site_url} {query}"
    )

    response = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        },
        json={
            "q": search_query,
            "num": num_results
        }
    )

    response.raise_for_status()

    data = response.json()

    results = []

    for item in data.get(
        "organic",
        []
    ):

        results.append(
            {
                "title": item.get(
                    "title",
                    ""
                ),
                "url": item.get(
                    "link",
                    ""
                )
            }
        )

    return results