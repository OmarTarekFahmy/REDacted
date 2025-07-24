import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_alert_email(user_ip: str):
    sender_email = os.getenv("ALERT_EMAIL_SENDER")
    receiver_email = os.getenv("ALERT_EMAIL_RECEIVER")
    password = os.getenv("ALERT_EMAIL_PASSWORD")

    # Create the email content
    subject = "Sensitive Info Detected in App Usage"
    body = f"""
    Alert: Sensitive information was detected.

    PII detected from {user_ip}
    """

    # Build the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send email using SMTP (Gmail example)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Error sending alert email: {e}")
