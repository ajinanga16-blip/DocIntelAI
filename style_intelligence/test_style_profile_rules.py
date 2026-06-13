from style_intelligence.style_profile_rules import (
    StyleProfileRules
)

rules_manager = (
    StyleProfileRules()
)

rules = [
    {
        "rule":
        "Use active voice"
    },
    {
        "rule":
        "Use sentence-case headings"
    }
]

rules_manager.save_rules(
    "Acme Style Guide",
    rules
)

loaded_rules = (
    rules_manager.load_rules(
        "Acme Style Guide"
    )
)

print(loaded_rules)