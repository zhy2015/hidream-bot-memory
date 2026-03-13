import smtplib
import ssl
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(to_email, subject, body, attachment_path):
    # Sender credentials (to be filled or passed as env)
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    username = os.environ.get("QQ_MAIL_USER")
    password = os.environ.get("QQ_MAIL_PASS")

    if not username or not password:
        print("Error: QQ_MAIL_USER and QQ_MAIL_PASS environment variables must be set.")
        sys.exit(1)

    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain", "utf-8"))

    # Attach file
    if os.path.exists(attachment_path):
        filename = os.path.basename(attachment_path)
        with open(attachment_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            msg.attach(part)
    else:
        print(f"Error: Attachment not found at {attachment_path}")
        sys.exit(1)

    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ctx) as server:
            server.login(username, password)
            server.send_message(msg)
        print(f"Success: Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python send_mail.py <to_email> <subject> <body> <attachment_path>")
        sys.exit(1)
    
    send_email_with_attachment(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
