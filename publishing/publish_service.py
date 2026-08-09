from publishing.publisher_factory import (
    PublisherFactory
)

from publishing.publish_result import (
    PublishRequest
)


class PublishService:

    def __init__(self):

        self.factory = (
            PublisherFactory()
        )

    def publish(
        self,
        request: PublishRequest
    ):

        publisher = (
            self.factory.get_publisher(
                request.destination
            )
        )

        if publisher is None:

            return {

                "success": False,

                "message": (
                    f"{request.destination} "
                    "is not supported."
                )

            }

        return publisher.publish(
            request
        )