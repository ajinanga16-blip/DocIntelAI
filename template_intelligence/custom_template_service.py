from template_intelligence.template_upload_service import (
    TemplateUploadService
)


class CustomTemplateService:

    def __init__(self):

        self.upload_service = (
            TemplateUploadService()
        )

    def get_custom_templates(
        self
    ):

        return (
            self.upload_service
            .get_templates()
        )