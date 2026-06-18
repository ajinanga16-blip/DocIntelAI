from template_intelligence.template_selector import (
    TemplateSelector
)

selector = (
    TemplateSelector()
)

print(
    selector.get_template_name(
        "User Guide"
    )
)

print(
    selector.get_template_name(
        "FAQ"
    )
)

print(
    selector.get_template_name(
        "API Guide"
    )
)