import re


def normalize_text(text):
    """
    Normalize text for Documentation Intelligence matching.

    Makes matching resilient across repositories.
    """

    if not text:
        return ""

    text = str(text).lower()

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    words = []

    for word in text.split():

        # Very lightweight stemming

        if word.endswith("ies"):
            word = word[:-3] + "y"

        elif word.endswith("ses"):
            word = word[:-2]

        elif word.endswith("s") and len(word) > 4:
            word = word[:-1]

        elif word.endswith("ing") and len(word) > 5:
            word = word[:-3]

        elif word.endswith("ed") and len(word) > 4:
            word = word[:-2]

        words.append(word)

    return " ".join(words)