from pathlib import Path


class LocalFolderPublisher:

    def publish(
        self,
        request
    ):
        """
        Publish documentation
        to a local folder.
        """

        output_path = Path(
            request.output_folder
        )

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        safe_name = (
            request.title
            .replace(" ", "_")
            .replace("/", "_")
        )

        file_path = (
            output_path /
            f"{safe_name}.md"
        )

        file_path.write_text(

            request.content,

            encoding="utf-8"

        )

        return {

            "success": True,

            "message": "Documentation published successfully.",

            "location": str(file_path)

        }