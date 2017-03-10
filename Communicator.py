import random
from twilio.rest import TwilioRestClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_text(to_number,from_number,body):
    twilio_account_sid = "AC99faeab4ac921d22d1ae19210d5853b2"
    twilio_auth_token = "4db2c7713c5b95af6c6842c4a7e698f5"
    client = TwilioRestClient(twilio_account_sid, twilio_auth_token)
    client.messages.create(to=to_number, from_=from_number, body=body)


def send_email(to_address,subject,body):
    fromaddr = "secretsantabotbchacks@gmail.com"
    toaddr = to_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "secretsanta")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

send_text("14259705093","14259705093","testing")