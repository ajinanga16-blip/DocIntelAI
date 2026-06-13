from style_intelligence.violation_schema import (
    VIOLATION_SCHEMA
)


class StyleRuleMatcher:

    def find_violations(
        self,
        document_content,
        rules
    ):

        violations = []

        for rule in rules:

            rule_text = rule.get(
                "rule",
                ""
            ).lower()

            if (
                "allow list instead of whitelist"
                in rule_text
            ):

                if (
                    "whitelist"
                    in document_content.lower()
                ):

                    violation = (
                        VIOLATION_SCHEMA.copy()
                    )

                    violation["category"] = (
                        "Terminology"
                    )

                    violation["rule"] = (
                        rule["rule"]
                    )

                    violation["violation"] = (
                        "Document uses whitelist."
                    )

                    violation["suggestion"] = (
                        "Replace whitelist with allow list."
                    )

                    violations.append(
                        violation
                    )

            if (
                "block list instead of blacklist"
                in rule_text
            ):

                if (
                    "blacklist"
                    in document_content.lower()
                ):

                    violation = (
                        VIOLATION_SCHEMA.copy()
                    )

                    violation["category"] = (
                        "Terminology"
                    )

                    violation["rule"] = (
                        rule["rule"]
                    )

                    violation["violation"] = (
                        "Document uses blacklist."
                    )

                    violation["suggestion"] = (
                        "Replace blacklist with block list."
                    )

                    violations.append(
                        violation
                    )

        return violations