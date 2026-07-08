from style_intelligence.document_compliance_service import (
    DocumentComplianceService
)

document = """
Create Forecast Variant

The master forecast can be copied.

The whitelist contains approved users.
"""

service = (
    DocumentComplianceService()
)

result = service.analyze(
    document,
    "Microsoft Technical Writing"
)

print(result)