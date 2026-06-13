from style_intelligence.violation_schema import (
    VIOLATION_SCHEMA
)

from style_intelligence.terminology_parser import (
    TerminologyParser
)


class StyleRuleMatcher:

    def __init__(self):

        self.parser = TerminologyParser()

    def find_violations(
        self,
        document_content,
        rules
    ):

        violations = []

        document_content_lower = (
            document_content.lower()
        )

        for rule in rules:

            rule_text = rule.get(
                "rule",
                ""
            )

            mapping = (
                self.parser.extract_term_mapping(
                    rule_text
                )
            )

            if not mapping:
                continue

            avoid_term = (
                mapping["avoid"]
                .lower()
            )

            preferred_term = (
                mapping["preferred"]
            )

            if avoid_term in document_content_lower:

                violation = (
                    VIOLATION_SCHEMA.copy()
                )

                violation["category"] = (
                    "Terminology"
                )

                violation["rule"] = (
                    rule_text
                )

                violation["violation"] = (
                    f"Document uses {avoid_term}."
                )

                violation["suggestion"] = (
                    f"Replace {avoid_term} with {preferred_term}."
                )

                violations.append(
                    violation
                )

        return violations