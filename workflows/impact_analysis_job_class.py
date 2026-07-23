from job_engine.base_intelligence_job import (
    BaseIntelligenceJob
)

from impact_analysis.impact_analysis_workflow import (
    analyze_impact_work_item
)


class ImpactAnalysisJob(BaseIntelligenceJob):

    def __init__(
        self,
        repository_name,
        work_items
    ):

        super().__init__(
            job_type="Impact Analysis",
            repository_name=repository_name
        )

        self.repository_name = repository_name
        self.work_items = work_items

    def execute(self):

        total = max(1, len(self.work_items))

        for index, work_item in enumerate(self.work_items):

            self.update_progress(

                progress=int(((index + 1) / total) * 100),

                message=f"Analyzing {index + 1}/{total}",

                current_step=index + 1,

                total_steps=total,

                current_phase="Impact Analysis",

                current_item=work_item.get(
                    "summary",
                    ""
                )

            )

        results = []

        for work_item in self.work_items:

            action_plan = analyze_impact_work_item(

                self.repository_name,

                work_item

            )

            results.append(action_plan)

        self.save_result(

            result_type="Documentation Action Plan",

            repository=self.repository_name,

            data=results

        )

        self.complete(

            message="Impact Analysis completed successfully.",

            result_type="Documentation Action Plan"

        )

        return self.job_id