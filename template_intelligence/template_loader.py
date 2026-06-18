import os


class TemplateLoader:

    def __init__(self):

        self.template_folder = (
            "templates"
        )

    def get_templates(self):

        if not os.path.exists(
            self.template_folder
        ):

            return []

        templates = []

        for file in os.listdir(
            self.template_folder
        ):

            if (
                file.endswith(".txt")
            ):

                templates.append(
                    file.replace(
                        ".txt",
                        ""
                    )
                )

        return sorted(
            templates
        )

    def load_template(
        self,
        template_name
    ):

        template_path = os.path.join(
            self.template_folder,
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