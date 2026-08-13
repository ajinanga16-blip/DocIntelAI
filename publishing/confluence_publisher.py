import base64
import html

import requests

from publishing.publish_result import (
    PublishResult
)


class ConfluencePublisher:

    def publish(
        self,
        request
    ):
        """
        Publish documentation to Confluence Cloud.
        """

        base_url = getattr(
            request,
            "base_url",
            None
        )

        email = getattr(
            request,
            "email",
            None
        )

        api_token = getattr(
            request,
            "api_token",
            None
        )

        space_key = getattr(
            request,
            "space_key",
            None
        )

        parent_id = getattr(
            request,
            "parent_id",
            None
        )

        title = getattr(
            request,
            "title",
            None
        )

        content = getattr(
            request,
            "content",
            None
        )

        #
        # Validate connection details
        #

        if not all(
            [
                base_url,
                email,
                api_token,
                space_key,
                title,
                content
            ]
        ):

            return PublishResult(

                success=False,

                message=(
                    "Missing Confluence "
                    "connection or document details."
                )

            ).to_dict()

        #
        # Normalize base URL
        #

        base_url = base_url.rstrip("/")

        #
        # Build authentication header
        #

        credentials = (
            f"{email}:{api_token}"
        )

        encoded_credentials = (
            base64.b64encode(
                credentials.encode("utf-8")
            ).decode("utf-8")
        )

        headers = {

            "Authorization":
            f"Basic {encoded_credentials}",

            "Accept":
            "application/json",

            "Content-Type":
            "application/json"

        }

        #
        # Convert Markdown-ish content
        # into safe Confluence storage HTML.
        #
        # Phase 1 intentionally keeps this
        # simple. We will improve Markdown
        # conversion later.
        #

        safe_content = html.escape(
            content
        )

        confluence_content = (
            f"<pre>{safe_content}</pre>"
        )

        #
        # Build page payload
        #

        payload = {

            "type":
            "page",

            "title":
            title,

            "space": {

                "key":
                space_key

            },

            "body": {

                "storage": {

                    "value":
                    confluence_content,

                    "representation":
                    "storage"

                }

            }

        }

        #
        # Optional parent page
        #

        if parent_id:

            payload["ancestors"] = [

                {

                    "id":
                    str(parent_id)

                }

            ]

        #
        # Publish
        #

        try:

            response = requests.post(

                (
                    f"{base_url}"
                    "/wiki/rest/api/content"
                ),

                headers=headers,

                json=payload,

                timeout=30

            )

        except requests.RequestException as error:

            return PublishResult(

                success=False,

                message=(
                    "Unable to connect to "
                    f"Confluence: {error}"
                )

            ).to_dict()

        #
        # Successful response
        #

        if response.status_code in (
            200,
            201
        ):

            try:

                page = response.json()

            except ValueError:

                return PublishResult(

                    success=True,

                    message=(
                        "Published to "
                        "Confluence successfully."
                    )

                ).to_dict()

            page_links = (
                page.get(
                    "_links",
                    {}
                )
            )

            web_ui = page_links.get(
                "webui"
            )

            page_url = None

            if web_ui:
                if web_ui.startswith("/wiki/"):

                    page_url = (
                        base_url
                        +
                        web_ui
                    )
                elif web_ui.startswith("/"):

                    page_url = (
                        base_url
                        +
                        "/wiki"
                        +
                        web_ui
                    )

                else:

                    page_url = (
                        base_url
                        +
                        "/wiki/"
                        +
                        web_ui
                    )

            return PublishResult(

                success=True,

                message=(
                    "Published to "
                    "Confluence successfully."
                ),

                url=page_url

            ).to_dict()

        #
        # Failed response
        #

        try:

            error_body = response.json()

            error_message = (
                error_body.get(
                    "message"
                )
                or
                error_body.get(
                    "error"
                )
                or
                response.text
            )

        except ValueError:

            error_message = (
                response.text
            )

        return PublishResult(

            success=False,

            message=(
                "Confluence publishing "
                f"failed ({response.status_code}): "
                f"{error_message}"
            )

        ).to_dict()