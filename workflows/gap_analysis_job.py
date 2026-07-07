from job_engine.base_intelligence_job import IntelligenceJob

from job_engine.job_manager import (
    JobManager
)

from gap_analysis.gap_analysis_workflow import (
    analyze_gap_tickets
)

from job_engine.job_results.result_manager import (
    save_job_result
)


def run_gap_analysis_job(
    repository_name,
    tickets
):
    """
    Runs Gap Analysis as a background job.
    """

    job_manager = JobManager()

    job = job_manager.create_job(

        job_type="Gap Analysis",

        repository_name=repository_name,

        notification_email=""

    )

    try:

        total = len(tickets)

        results = []

        for index, ticket in enumerate(tickets):

            progress = int(
                ((index + 1) / total) * 100
            )

            job_manager.update_progress(

                job["job_id"],

                progress=progress,

                message=f"Analyzing {index+1}/{total}",

                current_step=index + 1,

                total_steps=total,

                current_phase="Gap Analysis",

                current_item=ticket.get(
                    "summary",
                    ""
                )

            )

            result = analyze_gap_tickets(

                repository_name,

                [ticket]

            )

            results.extend(
                result
            )

        #
        # Save completed result
        #

        save_job_result(

            job_id=job["job_id"],

            result_type="Documentation Action Plan",

            repository=repository_name,

            data=results

        )

        job_manager.complete_job(

            job["job_id"],

            message="Gap Analysis completed successfully.",

            result_type="Documentation Action Plan",

            result_id=job["job_id"]

        )

        return job["job_id"]

    except Exception as ex:

        job_manager.fail_job(

            job["job_id"],

            str(ex)

        )

        raise