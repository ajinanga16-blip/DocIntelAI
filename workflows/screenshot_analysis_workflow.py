import json

from agents.screenshot_agent import (
    analyze_screenshot
)


def analyze_screenshot_workflow(
    screenshot_file
):
    """
    Extract structured information from a screenshot
    for downstream Help Site article discovery.
    """

    response = analyze_screenshot(
        screenshot_file,
        mode="discovery"
    )

    if isinstance(response, dict):
        return response

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:

        print(response)
        return json.loads(response)

    except Exception:

        return {
            "page_title": "",
            "screen_name": "",
            "breadcrumbs": [],
            "ui_elements": [],
            "buttons": [],
            "labels": [],
            "menus": [],
            "keywords": []
        }