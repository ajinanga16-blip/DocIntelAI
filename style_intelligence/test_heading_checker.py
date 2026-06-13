from style_intelligence.heading_checker import (
    HeadingChecker
)

checker = HeadingChecker()

document = """
# User Guide

## Create Forecast Variant

## overview

## Forecast Scenario Analysis
"""

results = (
    checker.find_heading_issues(
        document
    )
)

print(results)