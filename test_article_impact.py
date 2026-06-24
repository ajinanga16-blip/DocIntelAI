from agents.article_impact_agent import (
    analyze_cluster_impact
)

result = analyze_cluster_impact(
    "Navigation Role dropdown removed",
    "User Management",
    [
        "Assign User Role",
        "Create User"
    ]
)

print(result)