import datetime

import Communicator
import Scheduler

mailer_bot = "spamslamjamuw@gmail.com"
mailer_bot_password = "pleasehackme"

"""
Sends emails to a mailing list every month.
"""


def send_emails_at_end_of_month(recipients):
    while (True):
        today = datetime.date.today()
        if Scheduler.end_of_month(today.month, today.day, today.year):
            for recipient in recipients:
                Communicator.send_email(recipient, mailer_bot, mailer_bot_password, "Testing", "Body")

        Scheduler.sleepEveryXHours(6)
