import base64

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
        Publish documentation
        to Confluence Cloud.
        """

        if not all(
            [
                request.base_url,
                request.email,
                request.api_token,
                request.space_key
            ]
        ):

            return PublishResult(

                success=False,

                message=(
                    "Missing Confluence "
                    "connection details."
                )

            ).to_dict()

        auth = base64.b64encode(

            f"{request.email}:{request.api_token}".encode()

        ).decode()

        headers = {

            "Authorization": f"Basic {auth}",

            "Content-Type": "application/json"

        }

        payload = {

            "type": "page",

            "title": request.title,

            "space": {

                "key": request.space_key

            },

            "body": {

                "storage": {

                    "value": f"<pre>{request.content}</pre>",

                    "representation": "storage"

                }

            }

        }

        if request.parent_id:

            payload["ancestors"] = [

                {

                    "id": request.parent_id

                }

            ]

        response = requests.post(

            f"{request.base_url}/wiki/rest/api/content",

            headers=headers,

            json=payload,

            timeout=30

        )

        if response.status_code in (

            200,
            201

        ):

            page = response.json()

            return PublishResult(

                success=True,

                message=(
                    "Published to "
                    "Confluence successfully."
                ),

                url=(
                    request.base_url
                    +
                    page["_links"]["webui"]
                )

            ).to_dict()

        return PublishResult(

            success=False,

            message=response.text

        ).to_dict()