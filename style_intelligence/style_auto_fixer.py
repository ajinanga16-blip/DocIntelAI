import json
import os


class StyleAutoFixer:

    def __init__(self):

        fixes_path = os.path.join(
            os.path.dirname(__file__),
            "terminology_fixes.json"
        )

        with open(
            fixes_path,
            "r",
            encoding="utf-8"
        ) as file:

            self.terminology_fixes = (
                json.load(file)
            )

    def fix_document(
        self,
        document_content,
        violations
    ):

        corrected_content = (
            document_content
        )

        for violation in violations:

            category = violation.get(
                "category",
                ""
            )

            if (
                category
                ==
                "Inclusive Language"
            ):

                corrected_content = (
                    self._fix_inclusive_language(
                        corrected_content
                    )
                )

            elif (
                category
                ==
                "Heading Style"
            ):

                corrected_content = (
                    self._fix_heading_style(
                        corrected_content,
                        violation
                    )
                )

        return corrected_content

    def _fix_inclusive_language(
        self,
        content
    ):

        for (
            old_term,
            new_term
        ) in self.terminology_fixes.items():

            content = content.replace(
                old_term,
                new_term
            )

            content = content.replace(
                old_term.title(),
                new_term.title()
            )

        return content

    def _fix_heading_style(
        self,
        content,
        violation
    ):

        heading = violation.get(
            "violation",
            ""
        )

        if not heading:

            return content

        sentence_case = (
            heading[:1].upper()
            +
            heading[1:].lower()
        )

        return content.replace(
            heading,
            sentence_case
        )