from style_intelligence.style_checker import (
    StyleChecker
)

from style_intelligence.style_profile_service import (
    StyleProfileService
)

from style_intelligence.compliance_style_mapper import (
    ComplianceStyleMapper
)


class DocumentComplianceService:

    def analyze(
        self,
        document_content,
        style_name
    ):

        mapper = (
            ComplianceStyleMapper()
        )

        compliance_profile = (
            mapper.get_compliance_profile(
                style_name
            )
        )

        if not compliance_profile:

            return {
                "score":
                "Not Available",

                "violations":
                [],

                "message":
                "Compliance profile not available."
            }

        profile_service = (
            StyleProfileService()
        )

        checker = (
            StyleChecker()
        )

        rules = (
            profile_service.get_rules(
                compliance_profile
            )
        )

        return (
            checker.check_document(
                document_content,
                rules
            )
        )