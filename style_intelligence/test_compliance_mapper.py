from style_intelligence.document_compliance_service import (
    DocumentComplianceService
)

service = (
    DocumentComplianceService()
)

print(
    service.analyze(
        "Sample document",
        "IBM Technical Documentation"
    )
)