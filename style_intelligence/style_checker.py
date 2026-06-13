from style_intelligence.style_rule_matcher import (
    StyleRuleMatcher
)

from style_intelligence.passive_voice_checker import (
    PassiveVoiceChecker
)

from style_intelligence.inclusive_language_checker import (
    InclusiveLanguageChecker
)

from style_intelligence.heading_checker import (
    HeadingChecker
)

from style_intelligence.sentence_length_checker import (
    SentenceLengthChecker
)

from style_intelligence.style_score_engine import (
    StyleScoreEngine
)


class StyleChecker:

    def __init__(self):

        self.matcher = StyleRuleMatcher()

        self.passive_checker = (
            PassiveVoiceChecker()
        )

        self.inclusive_checker = (
            InclusiveLanguageChecker()
        )

        self.heading_checker = (
            HeadingChecker()
        )

        self.sentence_checker = (
            SentenceLengthChecker()
        )

        self.score_engine = (
            StyleScoreEngine()
        )

    def check_document(
        self,
        document_content,
        rules
    ):

        violations = []

        terminology_violations = (
            self.matcher.find_violations(
                document_content,
                rules
            )
        )

        violations.extend(
            terminology_violations
        )

        passive_findings = (
            self.passive_checker
            .find_passive_voice(
                document_content
            )
        )

        for finding in passive_findings:

            violations.append(
                {
                    "category":
                    "Passive Voice",

                    "rule":
                    "Use active voice",

                    "violation":
                    finding,

                    "suggestion":
                    "Rewrite using active voice.",

                    "severity":
                    "medium"
                }
            )

        inclusive_findings = (
            self.inclusive_checker
            .find_inclusive_language_issues(
                document_content
            )
        )

        for finding in inclusive_findings:

            violations.append(
                {
                    "category":
                    "Inclusive Language",

                    "rule":
                    "Use inclusive language",

                    "violation":
                    f"Document uses '{finding}'.",

                    "suggestion":
                    f"Replace '{finding}' with an inclusive alternative.",

                    "severity":
                    "high"
                }
            )

        heading_findings = (
            self.heading_checker
            .find_heading_issues(
                document_content
            )
        )

        for finding in heading_findings:

            violations.append(
                {
                    "category":
                    "Heading Style",

                    "rule":
                    "Use sentence-case headings",

                    "violation":
                    finding,

                    "suggestion":
                    "Convert heading to sentence case.",

                    "severity":
                    "medium"
                }
            )

        sentence_findings = (
            self.sentence_checker
            .find_long_sentences(
                document_content
            )
        )

        for finding in sentence_findings:

            violations.append(
                {
                    "category":
                    "Sentence Length",

                    "rule":
                    "Keep sentences concise",

                    "violation":
                    finding["sentence"],

                    "suggestion":
                    f"Sentence contains {finding['word_count']} words. Consider shortening it.",

                    "severity":
                    "low"
                }
            )

        score = (
            self.score_engine
            .calculate_score(
                violations
            )
        )

        return {
            "score": score,
            "violations": violations
        }