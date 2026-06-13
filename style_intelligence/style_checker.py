from style_intelligence.style_rule_matcher import (
    StyleRuleMatcher
)


class StyleChecker:

    def __init__(self):

        self.matcher = StyleRuleMatcher()

    def check_document(
        self,
        document_content,
        rules
    ):
        return self.matcher.find_violations(
    document_content,
    rules
)