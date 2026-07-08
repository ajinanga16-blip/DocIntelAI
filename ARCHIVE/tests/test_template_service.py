from template_intelligence.template_service import (
    TemplateService
)

service = (
    TemplateService()
)

template = (
    service.get_template(
        "User Guide"
    )
)

print(template)