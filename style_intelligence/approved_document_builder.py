from style_intelligence.style_auto_fixer import (
    StyleAutoFixer
)


class ApprovedDocumentBuilder:

    def __init__(self):

        self.auto_fixer = (
            StyleAutoFixer()
        )

    def build(
        self,
        original_document,
        suggestions
    ):
        """
        Build the approved document using
        only accepted suggestions.
        """

        accepted_violations = []

        for suggestion in suggestions:

            if (
                suggestion.get(
                    "status"
                )
                ==
                "Accepted"
            ):

                accepted_violations.append(

                    {

                        "category": suggestion.get(
                            "category",
                            ""
                        ),

                        "violation": suggestion.get(
                            "original",
                            ""
                        )

                    }

                )

        approved_document = (
            self.auto_fixer.fix_document(
                original_document,
                accepted_violations
            )
        )

        return approved_document