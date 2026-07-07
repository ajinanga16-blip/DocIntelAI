from workflows.gap_analysis_job_class import GapAnalysisJob


def run_gap_analysis_job(
    repository_name,
    tickets
):
    """
    Entry point for Gap Analysis.
    """

    job = GapAnalysisJob(
        repository_name,
        tickets
    )

    return job.execute()