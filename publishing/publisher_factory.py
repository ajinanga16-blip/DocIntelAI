from publishing.local_folder_publisher import (
    LocalFolderPublisher
)

from publishing.github_publisher import (
    GitHubPublisher
)

from publishing.mkdocs_publisher import (
    MkDocsPublisher
)

from publishing.docusaurus_publisher import (
    DocusaurusPublisher
)

from publishing.confluence_publisher import (
    ConfluencePublisher
)


class PublisherFactory:

    def get_publisher(
        self,
        destination
    ):

        if destination == "Local Folder":

            return (
                LocalFolderPublisher()
            )

        elif destination == "GitHub Repository":

            return (
                GitHubPublisher()
            )

        elif destination == "GitHub Pages":

            return (
                GitHubPublisher()
            )

        elif destination == "MkDocs":

            return (
                MkDocsPublisher()
            )

        elif destination == "Docusaurus":

            return (
                DocusaurusPublisher()
            )

        elif destination == "Confluence":

            return (
                ConfluencePublisher()
            )

        return None