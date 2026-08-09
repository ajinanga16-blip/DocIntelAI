class PublishRequest:

    def __init__(

        self,

        destination,

        title,

        content,

        output_folder=None,

        repository=None,

        branch="main",

        github_token=None,

        base_url=None,

        email=None,

        api_token=None,

        space_key=None,

        parent_id=None

    ):

        self.destination = destination

        self.title = title

        self.content = content

        self.output_folder = output_folder

        self.repository = repository

        self.branch = branch

        self.github_token = github_token

        self.base_url = base_url

        self.email = email

        self.api_token = api_token

        self.space_key = space_key

        self.parent_id = parent_id


class PublishResult:

    def __init__(

        self,

        success,

        message,

        location=None,

        url=None

    ):

        self.success = success

        self.message = message

        self.location = location

        self.url = url

    def to_dict(self):

        return {

            "success": self.success,

            "message": self.message,

            "location": self.location,

            "url": self.url

        }