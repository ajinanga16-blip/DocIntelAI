from agents.screenshot_change_agent import (
    summarize_screenshot_change
)

comparison_result = """
Added:
User Role page

Removed:
Navigation Role dropdown

Modified:
Navigation path changed

Old:
Create User > Assign User Role

New:
User Role > Assign User Role
"""

result = summarize_screenshot_change(
    comparison_result
)

print(
    result["change_summary"]
)

print(
    result["removed_elements"]
)

print(
    result["navigation_changes"]
)