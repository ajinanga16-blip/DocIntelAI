import os


class TemplateUploadService:

    def __init__(self):

        self.template_folder = (
            "custom_templates"
        )

        os.makedirs(
            self.template_folder,
            exist_ok=True
        )

    def save_template(
        self,
        uploaded_file
    ):

        file_path = os.path.join(
            self.template_folder,
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as file:

            file.write(
                uploaded_file.getbuffer()
            )

        return file_path

    def get_templates(
        self
    ):

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