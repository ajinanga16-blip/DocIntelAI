class PassiveVoiceChecker:

    PASSIVE_PATTERNS = [
        "was ",
        "were ",
        "is being ",
        "are being ",
        "has been ",
        "have been ",
        "had been ",
        "be "
    ]

    def find_passive_voice(
        self,
        document_content
    ):

        findings = []

        sentences = (
            document_content.split(".")
        )

        for sentence in sentences:

            sentence_lower = (
                sentence.lower()
            )

            for pattern in (
                self.PASSIVE_PATTERNS
            ):

                if pattern in sentence_lower:

                    findings.append(
                        sentence.strip()
                    )

                    break

        return findings