"""Email related functions."""

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    """Email object."""

    def send_mail(
        self,
        message_body: str,
        email_subject: str,
        email_from: str,
        email_to: str,
        path_to_csv_file: str,
        file_name: str,
        smtp_server: str,
        smtp_port: int,
        smtp_username: str,
        smtp_password: str,
    ):
        """Send email of data."""
        msg = MIMEMultipart()
        body_part = MIMEText(message_body, "plain")
        msg["Subject"] = email_subject
        msg["From"] = email_from
        msg["To"] = email_to
        msg.attach(body_part)
        with open(path_to_csv_file, "rb") as file:
            msg.attach(MIMEApplication(file.read(), Name=file_name))
        smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
        smtp_obj.login(smtp_username, smtp_password)
        smtp_obj.sendmail(msg["From"], msg["To"], msg.as_string())
        smtp_obj.quit()
