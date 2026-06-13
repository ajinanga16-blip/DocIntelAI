from style_intelligence.inclusive_language_checker import (
    InclusiveLanguageChecker
)

checker = InclusiveLanguageChecker()

document = """
Users can be added to a whitelist.

The master node controls the cluster.
"""

results = (
    checker.find_inclusive_language_issues(
        document
    )
)

print(results)