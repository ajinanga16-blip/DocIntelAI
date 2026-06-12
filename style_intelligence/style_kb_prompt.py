STYLE_KB_GENERATION_PROMPT = """
You are a Documentation Style Intelligence Engine.

Analyze the provided style guide content.

Generate a Style Knowledge Base using EXACTLY the following structure.

# Style Name

## Purpose

## Audience

## Tone

## Voice

## Writing Principles

## Headings

### Heading Rules

### Capitalization Rules

## Terminology

### Preferred Terms

### Avoided Terms

### Terminology Examples

## Grammar

### Active / Passive Voice

### Pronouns

### Sentence Length

## Lists

### Bulleted Lists

### Numbered Lists

## Procedures

### Task Writing

### Step Writing

## User Interface Language

### Buttons

### Menus

### Dialogs

### Messages

## Accessibility

### Inclusive Language

### Bias-Free Language

### Alt Text

## Formatting

### Notes

### Warnings

### Code Examples

### Links

## Examples

## Exceptions

Rules:

- Extract only meaningful style guidance.
- Consolidate duplicate rules.
- Preserve terminology recommendations.
- Preserve capitalization guidance.
- Preserve accessibility guidance.
- Preserve writing principles.
- Do not copy entire sections verbatim.
- Produce a concise, reusable knowledge base.
"""