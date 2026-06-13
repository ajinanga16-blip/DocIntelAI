class TerminologyParser:

    def extract_term_mapping(
        self,
        rule_text
    ):

        rule_text = rule_text.lower()

        if " instead of " not in rule_text:
            return None

        parts = rule_text.split(
            " instead of "
        )

        preferred = (
            parts[0]
            .replace("use ", "")
            .strip()
        )

        avoid = (
            parts[1]
            .strip()
        )

        return {
            "preferred": preferred,
            "avoid": avoid
        }