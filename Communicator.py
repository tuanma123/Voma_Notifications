import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import TwilioRestClient


class Communicator():
    def __init__(self, twilio_sid, twilio_auth_token, twilio_number, email_address, email_password):
        self.twilio_sid = twilio_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_number = twilio_number
        self.email_address = email_address
        self.email_password = email_password

    """
    Sends an individual text message to a phone using the Twilio API.

    @:param to_number: The number receiving the message.
    @:param from_number: The number sending the message.
    @:param body: The message of the text
    """
    def send_text(self, to_number, body):
        client = TwilioRestClient(self.twilio_sid, self.twilio_auth_token)
        client.messages.create(to = to_number, from_= self.twilio_number, body = body)

    """
    Sends an individual email message.

    @:param to_address: The recipient email address.
    @:param subject: The subject header of the email.
    @:param body: The body of the email.
    """

    def send_email(self, to_address, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_address
        msg['Subject'] = subject

        body = body
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email_address, self.email_password)
        text = msg.as_string()
        server.sendmail(self.email_address, to_address, text)
        server.quit()
        print("message sent")

    # Send a batch of emails given a list.
    def send_batch_email(self, email_list, subject, body):
        for email in email_list:
            self.send_email(email, subject, body)

    # Send a batch of messages given a list of phone numbers.
    def send_batch_message(self, msg_list, body):
        for phone_number in msg_list:
            self.send_text(phone_number, body)
