from style_intelligence.style_auto_fixer import (
    StyleAutoFixer
)

document = """
Create Forecast Variant

The master forecast can be copied.

The whitelist contains approved users.
"""

violations = [
    {
        "category":
        "Inclusive Language"
    },
    {
        "category":
        "Heading Style",

        "violation":
        "Create Forecast Variant"
    }
]

fixer = StyleAutoFixer()

result = fixer.fix_document(
    document,
    violations
)

print(result)