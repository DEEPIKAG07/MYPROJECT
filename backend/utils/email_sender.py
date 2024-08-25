import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    from_email = 'your-email@example.com'
    password = 'your-email-password'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
