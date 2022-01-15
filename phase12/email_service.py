import smtplib
import ssl


def format_message(content: str, sender: str):
    subject = "Verification Code"
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (
        content,
        sender,
        subject,
        content,
    )
    return email_text


class EmailService:
    sender_email: str
    sender_password: str
    context: object

    def __init__(self, sender_email: str, sender_password: str):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.context = ssl.create_default_context()

    def send_email(self, receiver_email: str, content: str):
        port = 587
        smtp_server = "smtp.gmail.com"
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(
                self.sender_email,
                receiver_email,
                format_message(content=content, sender=self.sender_email),
            )
