from style_intelligence.style_checker import (
    StyleChecker
)

rules = [
    {
        "rule":
        "Use allow list instead of whitelist"
    },
    {
        "rule":
        "Use block list instead of blacklist"
    }
]

document = """
Users can be added to a whitelist.

Blocked users are added
to a blacklist.
"""

checker = StyleChecker()

violations = checker.check_document(
    document,
    rules
)

print(violations)