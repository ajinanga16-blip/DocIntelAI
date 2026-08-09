from pathlib import Path

from publishing.publish_result import (
    PublishResult
)


class MkDocsPublisher:

    def publish(
        self,
        request
    ):
        """
        Generate a complete MkDocs documentation project.
        """

        if not request.output_folder:

            return PublishResult(

                success=False,

                message=(
                    "Please provide an output "
                    "folder for the MkDocs project."
                )

            ).to_dict()

        project_path = (
            Path(request.output_folder)
            / "mkdocs_project"
        )

        docs_path = (
            project_path
            / "docs"
        )

        docs_path.mkdir(
            parents=True,
            exist_ok=True
        )

        #
        # mkdocs.yml
        #

        mkdocs_config = (
            "site_name: "
            f'"{request.title}"\n\n'
            "nav:\n"
            "  - Home: index.md\n"
        )

        (
            project_path / "mkdocs.yml"
        ).write_text(
            mkdocs_config,
            encoding="utf-8"
        )

        #
        # Documentation
        #

        (
            docs_path / "index.md"
        ).write_text(
            request.content,
            encoding="utf-8"
        )

        #
        # README
        #

        readme_lines = [

            f"# {request.title}",

            "",

            "This documentation project was generated "
            "by DocIntel AI.",

            "",

            "## Run locally",

            "",

            "Install MkDocs:",

            "",

            "pip install mkdocs",

            "",

            "Start the documentation site:",

            "",

            "mkdocs serve",

            "",

            "Build the static site:",

            "",

            "mkdocs build"

        ]

        readme = "\n".join(
            readme_lines
        )

        (
            project_path / "README.md"
        ).write_text(
            readme,
            encoding="utf-8"
        )

        return PublishResult(

            success=True,

            message=(
                "MkDocs project "
                "generated successfully."
            ),

            location=str(
                project_path
            )

        ).to_dict()