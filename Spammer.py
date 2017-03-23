import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from twilio.rest import TwilioRestClient

import Database

mailer_bot = "spamslamjamuw@gmail.com"
mailer_bot_password = "pleasehackme"
twilio_auth_token = "ACd2c7cb9040bb920dbb196efbd6af7df7"
twilio_sid = "5efc50b214eb7a96361f046f0b4e9b8f"
twilio_number = 2069224468


def sleep_every_x_seconds(interval):
    time.sleep(interval)


def sleep_every_x_minutes(interval):
    sleep_every_x_seconds(interval * 60)


def sleep_every_x_hours(interval):
    sleep_every_x_minutes(interval * 60)


def sleep_every_x_days(interval):
    sleep_every_x_hours(interval * 24)


def sleep_every_x_weeks(interval):
    sleep_every_x_days(interval * 7)


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def end_of_month(month, day, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return day == 31
    elif month == 2:
        if is_leap_year(year):
            return day == 29
        else:
            return day == 28
    else:
        return day == 30


class Spammer():
    def __init__(self, twilio_sid, twilio_auth_token, twilio_number, email_address, email_password):
        """

        :param twilio_sid:
        :param twilio_auth_token:
        :param twilio_number:
        :param email_address:
        :param email_password:
        """
        self.twilio_sid = twilio_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_number = twilio_number
        self.email_address = email_address
        self.email_password = email_password

    def send_text(self, to_number, body):
        """

        :param to_number:
        :param body:
        :return:
        """
        client = TwilioRestClient(self.twilio_sid, self.twilio_auth_token)
        client.messages.create(to=to_number, from_=self.twilio_number, body=body)

    def send_email(self, to_address, subject, body):
        """

        :param to_address:
        :param subject:
        :param body:
        :return:
        """
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

    # Send a batch of emails given a list of addresses.
    def send_batch_email(self, email_list, subject, body):
        for email in email_list:
            self.send_email(email, subject, body)

    # Send a batch of messages given a list of phone numbers.
    def send_batch_message(self, msg_list, body):
        for phone_number in msg_list:
            self.send_text(phone_number, body)

    # Implement this
    def send_email_to_users(subject, body):
        user_list = Database.get_user_list()
        for user in user_list:
            pass

    # Implement this
    def send_text_to_users(body):
        user_list = Database.get_user_list()
        for user in user_list:
            pass
