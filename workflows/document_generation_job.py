from workflows.document_generation_job_class import (
    DocumentGenerationJob
)


def run_document_generation_job(
    repository_name,
    work_items,
    document_type,
    style_guide,
    template_selection
):
    """
    Entry point for Documentation Generation.
    """

    job = DocumentGenerationJob(
        repository_name=repository_name,
        work_items=work_items,
        document_type=document_type,
        style_guide=style_guide,
        template_selection=template_selection
    )

    return job.execute()