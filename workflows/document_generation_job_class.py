from job_engine.base_intelligence_job import BaseIntelligenceJob

from agents.jira_intelligence_agent import (
    build_structured_requirements
)

from agents.documentation_agent import (
    generate_documentation_from_requirements
)


class DocumentGenerationJob(BaseIntelligenceJob):

    def __init__(
        self,
        repository_name,
        work_items,
        document_type,
        style_guide,
        template_selection
    ):

        super().__init__(
            job_type="Documentation Generation",
            repository_name=repository_name
        )

        self.repository_name = repository_name
        self.work_items = work_items
        self.document_type = document_type
        self.style_guide = style_guide
        self.template_selection = template_selection

    def execute(self):

        total = len(self.work_items)

        generated_documents = []

        for index, work_item in enumerate(self.work_items):

            self.update_progress(

                progress=int(
                    ((index + 1) / total) * 100
                ),

                message=f"Generating {index + 1}/{total}",

                current_step=index + 1,

                total_steps=total,

                current_phase="Documentation Generation",

                current_item=work_item.get(
                    "summary",
                    ""
                )

            )

            structured_requirements = (

                build_structured_requirements(
                    work_item
                )

            )

            document = (

                generate_documentation_from_requirements(

                    structured_requirements,

                    self.document_type,

                    self.style_guide,

                    self.template_selection["source"],

                    self.template_selection["template"]

                )

            )

            generated_documents.append(

                {

                    "ticket_id": work_item.get(
                        "ticket_id",
                        ""
                    ),

                    "summary": work_item.get(
                        "summary",
                        ""
                    ),

                    "document_type": self.document_type,

                    "style_guide": self.style_guide,

                    "document": document

                }

            )

        self.save_result(

            result_type="Generated Documentation",

            repository=self.repository_name,

            data=generated_documents

        )

        self.complete(

            message="Documentation generated successfully.",

            result_type="Generated Documentation"

        )

        return generated_documents