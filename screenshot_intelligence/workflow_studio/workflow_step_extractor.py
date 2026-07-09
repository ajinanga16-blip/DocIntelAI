from workflows.screenshot_analysis_workflow import (
    analyze_screenshot_workflow
)


def extract_workflow_steps(
    screenshots
):
    """
    Analyze every screenshot
    and return ordered screen context.
    """

    workflow_steps = []

    for index, screenshot in enumerate(screenshots):

        context = analyze_screenshot_workflow(
            screenshot
        )

        workflow_steps.append(

            {
                "step": index + 1,
                "context": context
            }

        )

    return workflow_steps