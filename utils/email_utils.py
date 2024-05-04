from flask_mail import Message
from app import mail

def send_email(subject, recipients, html_content):
    try:
      msg = Message(subject, recipients=recipients)
      msg.html = html_content
      mail.send(msg)
      return True
    except Exception as e:
      return False
