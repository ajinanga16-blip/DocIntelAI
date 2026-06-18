from template_intelligence.template_service import (
    TemplateService
)

from template_intelligence.template_renderer import (
    TemplateRenderer
)

service = (
    TemplateService()
)

renderer = (
    TemplateRenderer()
)

template = (
    service.get_template(
        "User Guide"
    )
)

content_map = {

    "overview":
    "This guide explains forecast scenario variants.",

    "feature_description":
    "Users can create and compare forecast variants.",

    "capabilities":
    "- Create variants\n- Compare variants",

    "user_roles":
    "Planner\nApprover",

    "prerequisites":
    "Access to forecasting module",

    "procedure":
    "1. Open Forecast\n2. Create Variant",

    "expected_result":
    "Variant created successfully",

    "dependencies":
    "SCRUM-1",

    "related_information":
    "Forecast Planning Guide"
}

result = (
    renderer.render(
        template,
        content_map
    )
)

print(result)