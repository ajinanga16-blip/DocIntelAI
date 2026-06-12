from style_intelligence.kb_reviewer import (
    KBReviewer
)

sample_kb = """
- Use active voice.
- Use sentence-case headings.
- Use allow list instead of whitelist.
"""

reviewer = KBReviewer()

rules = reviewer.extract_rules(
    sample_kb
)

for rule in rules:

    print(rule)