import os

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

    def get_custom_template(
        self,
        template_name
    ):

        template_path = os.path.join(
            "custom_templates",
            f"{template_name}.txt"
        )

        if not os.path.exists(
            template_path
        ):

            return None

        with open(
            template_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()