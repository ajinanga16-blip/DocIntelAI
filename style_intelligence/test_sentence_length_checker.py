from style_intelligence.sentence_length_checker import (
    SentenceLengthChecker
)

checker = (
    SentenceLengthChecker()
)

document = """
This is a short sentence.

This is a very long sentence that contains many words and is intentionally written to exceed the maximum sentence length threshold so that the checker can detect it correctly and report a violation.
"""

results = (
    checker.find_long_sentences(
        document
    )
)

print(results)