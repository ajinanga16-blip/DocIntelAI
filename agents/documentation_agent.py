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
def get_base_sections():

    return """
ALWAYS INCLUDE THE FOLLOWING INFORMATION
WHEN AVAILABLE:

- Feature Name
- Feature Description
- Key Capabilities
- Documentation Notes
- Implementation Notes
- Dependencies
- Attachments

Do not omit these sections unless the
information is unavailable.
"""
def get_document_template(document_type):

    templates = {

        "User Guide": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# User Guide

## Overview

## Feature Description

## Capabilities

## User Roles

## Dependencies

## Attachments

## Missing Information

Do not rename headings.
Do not omit sections.
""",

        
"FAQ": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# FAQ

## Overview

## Confirmed FAQs

For every confirmed FAQ use:

Q: <question>

A: <answer>

## Potential FAQs

For every potential FAQ use:

Q: <question>

A: [TODO: Information not provided in Jira]

## Missing Information

Do not include:

- Feature Name
- Feature Description
- Documentation Notes
- Implementation Notes
- Dependencies
- Attachments

unless directly needed in an answer.

Do not rename headings.
Do not omit sections.
""",

        "Release Notes": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# Release Notes

## Feature Name

## Feature Description

## Key Capabilities

## Release Summary

## Previous State

If unknown:
[TODO: Previous behavior not provided in Jira]

## Current State

## Business Value

If unknown:
[TODO: Business value not provided in Jira]

## Impacted Users

## Documentation Notes

## Implementation Notes

## Dependencies

## Attachments

## Known Limitations

If unknown:
[TODO: Known limitations not provided in Jira]

## Missing Information

Do not omit any section.
Do not rename any heading.
""",

"Knowledge Base": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# Knowledge Base

## Overview

## Feature Summary

## Key Capabilities

## Common Questions

Use:

Q: <question>

A: <answer>

## Dependencies

## Related Information

## Attachments

## Missing Information

Do not rename headings.
Do not omit sections.
""",

        "Quick Start Guide": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# Quick Start Guide

## Overview

## Feature Description

## Key Capabilities

## Getting Started

If workflow information is unavailable:

[TODO: Workflow steps require SME confirmation]

## Dependencies

## Attachments

## Missing Information

Do not rename headings.
Do not omit sections.
""",

        "Video Script": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# Video Script

## Introduction

## Feature Overview

## Key Capabilities

## Demonstration Steps

If workflow information is unavailable:

[TODO: Workflow steps require SME confirmation]

## Business Value

If unavailable:

[TODO: Business value not provided in Jira]

## Closing Summary

## Missing Information

Do not rename headings.
Do not omit sections.
""",

        "Solution Article": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# Solution Article

## Problem Statement

## Solution Overview

## Key Capabilities

## Benefits

## Dependencies

## Attachments

## Missing Information

Do not rename headings.
Do not omit sections.
""",

        "API Guide": """
OUTPUT FORMAT REQUIREMENT

Use EXACTLY these headings.

# API Guide

## API Overview

## Purpose

## Authentication / Authorization

If unavailable:

[TODO: Authentication details not provided in Jira]

## Endpoints

If unavailable:

[TODO: Endpoint details not provided in Jira]

## Request Parameters

If unavailable:

[TODO: Request parameters not provided in Jira]

## Request Example

If unavailable:

[TODO: Request example not provided in Jira]

## Response Details

If unavailable:

[TODO: Response details not provided in Jira]

## Response Example

If unavailable:

[TODO: Response example not provided in Jira]

## Error Codes

If unavailable:

[TODO: Error codes not provided in Jira]

## Rate Limits

If unavailable:

[TODO: Rate limit information not provided in Jira]

## Dependencies

## Related APIs

If unavailable:

[TODO: Related APIs not provided in Jira]

## Known Limitations

## Missing Information

Do not rename headings.
Do not omit sections.
""",
    }

    return templates.get(
        document_type,
        templates["User Guide"]
    )

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

    document_template = get_document_template(
        document_type
    )

    if document_type in [
        "Release Notes",
        "Knowledge Base",
        "API Guide"
    ]:
        base_sections = get_base_sections()
    else:
        base_sections = ""

    documentation_input += f"""

Document Type:
{document_type}

DOCUMENT STRUCTURE

{base_sections}

{document_template}

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