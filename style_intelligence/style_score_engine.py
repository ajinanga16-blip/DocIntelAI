class StyleScoreEngine:

    def calculate_score(
        self,
        violations
    ):

        score = 100

        for violation in violations:

            severity = violation.get(
                "severity",
                "low"
            )

            if severity == "high":

                score -= 10

            elif severity == "medium":

                score -= 5

            elif severity == "low":

                score -= 2

        return max(
            score,
            0
        )