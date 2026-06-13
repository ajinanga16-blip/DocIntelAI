class InclusiveLanguageChecker:

    TERMS_TO_AVOID = [
        "master",
        "slave",
        "whitelist",
        "blacklist"
    ]

    def find_inclusive_language_issues(
        self,
        document_content
    ):

        findings = []

        document_lower = (
            document_content.lower()
        )

        for term in (
            self.TERMS_TO_AVOID
        ):

            if term in document_lower:

                findings.append(term)

        return findings