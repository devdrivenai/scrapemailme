from datetime import date
import smtplib, ssl
from email.message import EmailMessage

def make_up_message(info, subject):
    today = date.today()
    message = EmailMessage()
    message.set_content(f'This is the data retrieved on {today}:\n{info}')
    message['Subject'] = subject
    # returns 'str'
    return message

def send_email(info, subject, email_config):
    message = make_up_message(info, subject)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(email_config['host'], email_config['port'], context=context) as server:
        server.login(email_config['username'], email_config['password'])
        server.send_message(message, email_config['username'], email_config['receiver'])