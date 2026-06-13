from style_intelligence.style_score_engine import (
    StyleScoreEngine
)

violations = [
    {
        "severity": "high"
    },
    {
        "severity": "medium"
    },
    {
        "severity": "medium"
    },
    {
        "severity": "low"
    }
]

engine = (
    StyleScoreEngine()
)

score = (
    engine.calculate_score(
        violations
    )
)

print(score)