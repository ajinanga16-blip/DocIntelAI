from style_intelligence.document_compliance_service import (
    DocumentComplianceService
)

document = """
Even though the autumn leaves were swirling violently through the cold, darkening evening sky, the team continued working on the release because they wanted to finish everything before the deadline and ensure all requirements were properly documented.
"""

service = (
    DocumentComplianceService()
)

result = service.analyze(
    document,
    "Microsoft Technical Writing"
)

print(result["score"])
print(result["corrected_score"])
print(result["corrected_violations"])