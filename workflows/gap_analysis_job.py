from job_engine.base_intelligence_job import BaseIntelligenceJob

from gap_analysis.gap_analysis_workflow import (
    analyze_gap_tickets
)


def run_gap_analysis_job(
    repository_name,
    tickets
):
    """
    Runs Gap Analysis as a background job.
    """

    job = BaseIntelligenceJob(
        job_type="Gap Analysis",
        repository_name=repository_name
    )

    try:

        total = len(tickets)
        results = []

        for index, ticket in enumerate(tickets):

            progress = int(((index + 1) / total) * 100)

            job.update_progress(
                progress=progress,
                message=f"Analyzing {index + 1}/{total}",
                current_step=index + 1,
                total_steps=total,
                current_phase="Gap Analysis",
                current_item=ticket.get("summary", "")
            )

            result = analyze_gap_tickets(
                repository_name,
                [ticket]
            )

            results.extend(result)

        job.save_result(
            result_type="Documentation Action Plan",
            repository=repository_name,
            data=results
        )

        job.complete(
            message="Gap Analysis completed successfully.",
            result_type="Documentation Action Plan"
        )

        return job.job_id

    except Exception as ex:

        job.fail(ex)
        raise