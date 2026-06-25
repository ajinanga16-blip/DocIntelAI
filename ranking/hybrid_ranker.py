import re

from ranking.synonym_dictionary import (
    SYNONYMS
)

from ranking.confidence_calculator import (
    calculate_confidence
)


def normalize(text):

    if not text:
        return ""

    return text.lower()


def tokenize(text):

    return set(
        re.findall(
            r"[a-zA-Z0-9]+",
            normalize(text)
        )
    )


def expand_terms(query):

    expanded = set()

    words = tokenize(query)

    expanded.update(words)

    expanded.add(query.lower())

    for word in list(words):

        if word in SYNONYMS:

            expanded.update(
                SYNONYMS[word]
            )

    return expanded


def rank_articles(
    queries,
    articles
):

    ranked = []

    expanded_queries = set()

    for query in queries:

        expanded_queries.update(
            expand_terms(query)
        )

    for article in articles:

        title = normalize(
            article.get(
                "title",
                ""
            )
        )

        content = normalize(
            article.get(
                "content",
                ""
            )
        )

        title_tokens = tokenize(title)

        content_tokens = tokenize(content)

        title_matches = (
            expanded_queries &
            title_tokens
        )

        content_matches = (
            expanded_queries &
            content_tokens
        )

        scores = {

            "title": 0,
            "content": 0,
            "keyword": 0,
            "ui": 0,
            "page": 0

        }

        matched_on = []

        #
        # Title
        #

        if title_matches:

            scores["title"] = 1

            matched_on.append(
                "Title"
            )

        #
        # Content
        #

        if len(content_matches) >= 3:

            scores["content"] = 1

            matched_on.append(
                "Content"
            )

        #
        # Keyword density
        #

        density = (
            len(content_matches)
            /
            max(
                len(expanded_queries),
                1
            )
        )

        scores["keyword"] = min(
            density,
            1
        )

        if density > 0:

            matched_on.append(
                "Keywords"
            )

        confidence = calculate_confidence(
            scores
        )

        if confidence > 15:

            article["confidence"] = confidence

            article["matched_on"] = sorted(
                matched_on
            )

            article["matched_terms"] = sorted(
                list(
                    title_matches |
                    content_matches
                )
            )

            ranked.append(
                article
            )

    ranked.sort(

        key=lambda x: (
            x["confidence"],
            len(
                x.get(
                    "matched_terms",
                    []
                )
            )
        ),

        reverse=True

    )

    return ranked