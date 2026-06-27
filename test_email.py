from notifications.email_service import send_email

response = send_email(
    "ajinanga16@gmail.com",
    "DocIntel AI Test",
    "<h2>Congratulations!</h2><p>Your first email from DocIntel AI was sent successfully.</p>"
)

print(response)