class HeadingChecker:

    def find_heading_issues(
        self,
        document_content
    ):

        findings = []

        lines = (
            document_content.splitlines()
        )

        for line in lines:

            line = line.strip()

            if not line.startswith("#"):
                continue

            heading = (
                line.replace("#", "")
                .strip()
            )

            if not heading:
                continue

            words = heading.split()

            if len(words) < 3:
                continue

            for word in words[1:]:

                if word[0].isupper():

                    findings.append(
                        heading
                    )

                    break

        return findings