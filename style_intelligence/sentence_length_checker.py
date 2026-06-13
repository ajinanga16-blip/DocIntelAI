class SentenceLengthChecker:

    MAX_WORDS = 25

    def find_long_sentences(
        self,
        document_content
    ):

        findings = []

        sentences = (
            document_content.split(".")
        )

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            word_count = len(
                sentence.split()
            )

            if (
                word_count >
                self.MAX_WORDS
            ):

                findings.append(
                    {
                        "sentence":
                        sentence,

                        "word_count":
                        word_count
                    }
                )

        return findings