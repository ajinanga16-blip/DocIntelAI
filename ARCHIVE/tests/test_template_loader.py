from template_intelligence.template_loader import (
    TemplateLoader
)

loader = (
    TemplateLoader()
)

print(
    loader.get_templates()
)

print(
    loader.load_template(
        "user_guide_template"
    )
)