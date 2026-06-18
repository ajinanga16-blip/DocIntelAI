from template_intelligence.template_loader import (
    TemplateLoader
)

from template_intelligence.template_selector import (
    TemplateSelector
)


class TemplateService:

    def __init__(self):

        self.loader = (
            TemplateLoader()
        )

        self.selector = (
            TemplateSelector()
        )

    def get_template(
        self,
        document_type
    ):

        template_name = (
            self.selector
            .get_template_name(
                document_type
            )
        )

        if not template_name:

            return None

        return (
            self.loader
            .load_template(
                template_name
            )
        )