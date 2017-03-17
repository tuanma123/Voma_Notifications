import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from twilio.rest import TwilioRestClient

"""
Sends a text message to a phone using the Twilio API.

@:param to_number: The number receiving the message.
@:param from_number: The number sending the message.
@:param body: The message of the text
"""
def send_text(to_number,from_number,body):
    twilio_account_sid = "AC99faeab4ac921d22d1ae19210d5853b2"
    twilio_auth_token = "4db2c7713c5b95af6c6842c4a7e698f5"
    client = TwilioRestClient(twilio_account_sid, twilio_auth_token)
    client.messages.create(to=to_number, from_=from_number, body=body)


"""
Sends an email message.

@:param to_address: The recipient email address.
@:param subject: The subject header of the email.
@:param body: The body of the email.
"""


def send_email(to_address, from_address, from_adress_password, subject,body):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, from_adress_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
    print("message sent")