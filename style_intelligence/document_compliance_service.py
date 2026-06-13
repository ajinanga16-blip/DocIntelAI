from style_intelligence.style_checker import (
    StyleChecker
)

from style_intelligence.style_profile_service import (
    StyleProfileService
)


class DocumentComplianceService:

    def analyze(
        self,
        document_content,
        style_name
    ):

        profile_service = (
            StyleProfileService()
        )

        checker = (
            StyleChecker()
        )

        rules = (
            profile_service.get_rules(
                style_name
            )
        )

        return (
            checker.check_document(
                document_content,
                rules
            )
        )