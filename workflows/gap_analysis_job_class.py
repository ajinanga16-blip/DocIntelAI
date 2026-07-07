from job_engine.base_intelligence_job import BaseIntelligenceJob

from gap_analysis.gap_analysis_workflow import analyze_gap_tickets


class GapAnalysisJob(BaseIntelligenceJob):

    def __init__(self, repository_name, tickets):
        super().__init__(
            job_type="Gap Analysis",
            repository_name=repository_name
        )

        self.repository_name = repository_name
        self.tickets = tickets

    def execute(self):

        total = len(self.tickets)
        results = []

        for index, ticket in enumerate(self.tickets):

            self.update_progress(
                progress=int(((index + 1) / total) * 100),
                message=f"Analyzing {index + 1}/{total}",
                current_step=index + 1,
                total_steps=total,
                current_phase="Gap Analysis",
                current_item=ticket.get("summary", "")
            )

            results.extend(
                analyze_gap_tickets(
                    self.repository_name,
                    [ticket]
                )
            )

        self.save_result(
            result_type="Documentation Action Plan",
            repository=self.repository_name,
            data=results
        )

        self.complete(
            message="Gap Analysis completed successfully.",
            result_type="Documentation Action Plan"
        )

        return self.job_id