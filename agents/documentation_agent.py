from styles.style_loader import get_style_profile

from agents.content_agent import (
    generate_documentation
)

from template_intelligence.template_service import (
    TemplateService
)


def build_documentation_input(
    structured_requirements
):

    acceptance_criteria = "\n".join(
        [
            f"- {item}"
            for item in structured_requirements.get(
                "acceptance_criteria",
                []
            )
        ]
    )

    documentation_notes = "\n".join(
        [
            f"- {item}"
            for item in structured_requirements.get(
                "documentation_notes",
                []
            )
        ]
    )

    implementation_notes = "\n".join(
        [
            f"- {item}"
            for item in structured_requirements.get(
                "implementation_notes",
                []
            )
        ]
    )

    dependencies = "\n".join(
        [
            f"- {item['key']}: {item['summary']}"
            for item in structured_requirements.get(
                "dependencies",
                []
            )
        ]
    )

    attachments = "\n".join(
        [
            f"- {item}"
            for item in structured_requirements.get(
                "attachments",
                []
            )
        ]
    )

    return f"""
You are generating documentation from structured Jira requirements.

GROUNDING RULES

Use ONLY information explicitly provided below.

DO NOT invent:

- Screens
- Buttons
- Menus
- Navigation paths
- UI labels
- Step-by-step procedures
- User instructions
- Click actions
- Workflows
- Sequences of actions
- Configuration settings
- Workflow steps
- User actions not explicitly stated
- System behavior not explicitly stated

If required information is missing,
insert a TODO placeholder.

Examples:

[TODO: Navigation path not provided]

[TODO: Screenshot not available]

[TODO: Workflow steps require SME confirmation]

Feature Name:
{structured_requirements.get('feature_name', '')}

Feature Description:
{structured_requirements.get('feature_description', '')}

Acceptance Criteria:
{acceptance_criteria}

Documentation Notes:
{documentation_notes}

Implementation Notes:
{implementation_notes}

Dependencies:
{dependencies}

Attachments:
{attachments}
"""


def generate_documentation_from_requirements(
    structured_requirements,
    document_type,
    style_guide,
    template_source="Built-in",
    template_name=None
):

    documentation_input = (
        build_documentation_input(
            structured_requirements
        )
    )

    style_profile = (
        get_style_profile(
            style_guide
        )
    )

    template_service = (
        TemplateService()
    )

    if (
        template_source
        ==
        "Custom"
        and
        template_name
    ):

        template_content = (
            template_service
            .get_custom_template(
                template_name
            )
        )

    else:

        template_content = (
            template_service
            .get_template(
                document_type
            )
        )

    documentation_input += f"""

DOCUMENT TYPE

{document_type}

TEMPLATE STRUCTURE

Use the following template structure exactly.

{template_content}

STYLE GUIDE

Style Name:
{style_profile['name']}

STYLE KNOWLEDGE BASE

{style_profile['knowledge_base']}

IMPORTANT RULES

- Follow the template exactly.
- Do not rename headings.
- Do not remove sections.
- Populate sections using available information.
- If information is unavailable, insert a TODO placeholder.
- Do not invent information.
"""

    return generate_documentation(
        documentation_input,
        document_type
    )