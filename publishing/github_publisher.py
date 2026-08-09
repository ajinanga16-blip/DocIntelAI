import base64

import requests

from publishing.publish_result import (
    PublishResult
)


class GitHubPublisher:

    def publish(
        self,
        request
    ):
        """
        Publish a Markdown document
        to a GitHub repository.
        """

        if not request.repository:

            return PublishResult(

                success=False,

                message=(
                    "GitHub repository is required."
                )

            ).to_dict()

        if not request.github_token:

            return PublishResult(

                success=False,

                message=(
                    "GitHub Personal Access Token "
                    "is required."
                )

            ).to_dict()

        repository = (
            request.repository
            .strip()
            .rstrip("/")
        )

        if repository.startswith(
            "https://github.com/"
        ):

            repository = repository[
                len("https://github.com/"):
            ]

        if repository.endswith(
            ".git"
        ):

            repository = repository[
                :-4
            ]

        parts = repository.split("/")

        if len(parts) != 2:

            return PublishResult(

                success=False,

                message=(
                    "Repository must be in "
                    "owner/repository format."
                )

            ).to_dict()

        owner = parts[0]

        repo = parts[1]

        file_name = (
            request.title
            .strip()
            .replace(" ", "_")
            .replace("/", "_")
        )

        path = (
            f"docs/{file_name}.md"
        )

        api_url = (
            f"https://api.github.com/repos/"
            f"{owner}/{repo}/contents/{path}"
        )

        headers = {

            "Accept":
                "application/vnd.github+json",

            "Authorization":
                f"Bearer {request.github_token}",

            "X-GitHub-Api-Version":
                "2022-11-28"

        }

        #
        # Check whether the file already exists.
        #

        existing_response = requests.get(

            api_url,

            headers=headers,

            params={
                "ref": request.branch
            },

            timeout=30

        )

        sha = None

        if existing_response.status_code == 200:

            existing_file = (
                existing_response.json()
            )

            sha = existing_file.get(
                "sha"
            )

        elif existing_response.status_code != 404:

            return PublishResult(

                success=False,

                message=(
                    "Unable to access the "
                    "GitHub repository: "
                    f"{existing_response.text}"
                )

            ).to_dict()

        #
        # Encode Markdown content.
        #

        encoded_content = base64.b64encode(

            request.content.encode(
                "utf-8"
            )

        ).decode(
            "utf-8"
        )

        payload = {

            "message": (
                f"Publish documentation: "
                f"{request.title}"
            ),

            "content": encoded_content,

            "branch": request.branch

        }

        if sha:

            payload["sha"] = sha

        #
        # Create or update the file.
        #

        response = requests.put(

            api_url,

            headers=headers,

            json=payload,

            timeout=30

        )

        if response.status_code in (
            200,
            201
        ):

            return PublishResult(

                success=True,

                message=(
                    "Documentation published "
                    "to GitHub successfully."
                ),

                url=(
                    f"https://github.com/"
                    f"{owner}/{repo}/blob/"
                    f"{request.branch}/{path}"
                )

            ).to_dict()

        return PublishResult(

            success=False,

            message=(
                "GitHub publishing failed: "
                f"{response.text}"
            )

        ).to_dict()