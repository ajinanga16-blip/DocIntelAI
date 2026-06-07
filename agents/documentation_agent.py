from agents.content_agent import generate_documentation


def build_documentation_input(
    structured_requirements
):
    """
    Convert structured requirements into
    a documentation-ready prompt with
    grounding instructions.
    """

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

DOCUMENTATION STYLE

If procedural steps are not explicitly provided,
do NOT generate numbered instructions.

Instead describe capabilities using known facts.

Example:

GOOD

- Users can create a variant from an existing forecast.
- Users can rename a variant.

BAD

1. Open Forecasts.
2. Select Create Variant.
3. Save changes.

If required information is missing, insert a TODO placeholder.

Examples:

[TODO: Navigation path not provided in Jira]

[TODO: Screenshot not available]

[TODO: Workflow steps require SME confirmation]

The goal is grounded documentation based on known facts.

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
    document_type
):
    """
    Generate documentation from
    structured Jira requirements.
    """

    documentation_input = (
        build_documentation_input(
            structured_requirements
        )
    )

    documentation_input += f"""

Document Type:
{document_type}

IMPORTANT:

Generate documentation using ONLY
the information provided.

If information required for a complete
document is missing, insert a TODO
placeholder rather than inventing content.

Examples:

[TODO: Navigation path not provided in Jira]

[TODO: Screenshot not available]

[TODO: Workflow steps require SME confirmation]
"""

    return generate_documentation(
        documentation_input,
        document_type
    )