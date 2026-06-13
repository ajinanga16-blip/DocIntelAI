from style_intelligence.custom_style_manager import (
    CustomStyleManager
)

manager = (
    CustomStyleManager()
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

manager.create_style_profile(
    "Acme Style Guide",
    "acme_style.md",
    rules
)

profile = (
    manager.load_style_profile(
        "Acme Style Guide"
    )
)

print(profile)