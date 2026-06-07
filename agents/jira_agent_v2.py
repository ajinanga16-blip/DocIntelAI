from jira import JIRA


class JiraAgentV2:
    def __init__(
        self,
        jira_url: str,
        email: str,
        api_token: str
    ):
        self.client = JIRA(
            server=jira_url,
            basic_auth=(email, api_token)
        )

    def get_issue_data(self, issue_key: str):
        """
        Retrieve structured issue data from Jira.
        """

        issue = self.client.issue(issue_key)

        summary = issue.fields.summary

        description = (
            issue.fields.description
            if hasattr(issue.fields, "description")
            else ""
        )

        comments = []

        if hasattr(issue.fields, "comment"):
            for comment in issue.fields.comment.comments:
                comments.append(
                    {
                        "author": comment.author.displayName,
                        "body": comment.body,
                        "created": str(comment.created)
                    }
                )

        linked_tickets = []

        if hasattr(issue.fields, "issuelinks"):
            for link in issue.fields.issuelinks:

                if hasattr(link, "outwardIssue"):
                    linked_tickets.append(
                        {
                            "key": link.outwardIssue.key,
                            "summary": link.outwardIssue.fields.summary,
                            "direction": "outward"
                        }
                    )

                elif hasattr(link, "inwardIssue"):
                    linked_tickets.append(
                        {
                            "key": link.inwardIssue.key,
                            "summary": link.inwardIssue.fields.summary,
                            "direction": "inward"
                        }
                    )

        attachments = []

        if hasattr(issue.fields, "attachment"):
            for attachment in issue.fields.attachment:
                attachments.append(
                    {
                        "filename": attachment.filename,
                        "size": attachment.size,
                        "mime_type": attachment.mimeType,
                        "content_url": attachment.content
                    }
                )

        return {
            "issue_key": issue.key,
            "summary": summary,
            "description": description,
            "comments": comments,
            "linked_tickets": linked_tickets,
            "attachments": attachments
        }