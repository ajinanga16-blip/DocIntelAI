from style_intelligence.rule_schema import (
    RULE_SCHEMA
)


class KBReviewer:

    def extract_rules(
        self,
        kb_content
    ):

        rules = []

        for line in kb_content.splitlines():

            line = line.strip()

            if line.startswith("- "):

                rule = RULE_SCHEMA.copy()

                rule["rule"] = (
                    line.replace("- ", "")
                )

                rules.append(rule)

        return rules

    def approve_rule(
        self,
        rule
    ):

        rule["status"] = "approved"

        return rule

    def reject_rule(
        self,
        rule
    ):

        rule["status"] = "rejected"

        return rule

    def build_approved_kb(
        self,
        approved_rules
    ):

        return approved_rules