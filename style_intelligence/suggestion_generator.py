class SuggestionGenerator:

    def build_suggestions(
        self,
        compliance_result
    ):

        suggestions = []

        for index, violation in enumerate(
            compliance_result.get(
                "violations",
                []
            )
        ):

            suggestions.append(

                {

                    "id": index + 1,

                    "category": violation.get(
                        "category",
                        ""
                    ),

                    "rule": violation.get(
                        "rule",
                        ""
                    ),

                    "original": violation.get(
                        "violation",
                        ""
                    ),

                    "suggestion": violation.get(
                        "suggestion",
                        ""
                    ),

                    "status": "Pending"

                }

            )

        return suggestions