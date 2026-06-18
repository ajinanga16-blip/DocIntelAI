class TemplateRenderer:

    def render(
        self,
        template_content,
        content_map
    ):

        rendered_content = (
            template_content
        )

        for (
            placeholder,
            value
        ) in content_map.items():

            rendered_content = (
                rendered_content.replace(
                    f"{{{{{placeholder}}}}}",
                    value
                )
            )

        return rendered_content