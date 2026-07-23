from workflows.impact_analysis_job_class import (
    ImpactAnalysisJob
)


def run_impact_analysis_job(
    repository_name,
    work_items
):
    """
    Entry point for Impact Analysis.
    """

    job = ImpactAnalysisJob(
        repository_name,
        work_items
    )

    return job.execute()