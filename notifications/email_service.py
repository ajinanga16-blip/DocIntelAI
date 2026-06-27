import os

import resend
from dotenv import load_dotenv


load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(to_email, subject, html):

    params = {
        "from": os.getenv("FROM_EMAIL"),
        "to": [to_email],
        "subject": subject,
        "html": html
    }

    return resend.Emails.send(params)