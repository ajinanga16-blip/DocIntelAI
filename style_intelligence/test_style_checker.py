from style_intelligence.style_checker import (
    StyleChecker
)

rules = [
    {
        "rule":
        "Use allow list instead of whitelist"
    }
]

document = """
# Create Forecast Variant

The report was generated automatically.

Users can be added to a whitelist.

The master node controls the cluster.

Even though the autumn leaves were swirling violently through the cold, darkening evening sky, he stubbornly refused to abandon his search for the lost journal, which held all the answers he desperately needed before the impending snowstorm completely buried the rugged mountain trail.
"""

checker = StyleChecker()

results = checker.check_document(
    document,
    rules
)

print(results)