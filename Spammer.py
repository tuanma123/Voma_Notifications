import datetime
import time

import Communicator
import Database

mailer_bot = "spamslamjamuw@gmail.com"
mailer_bot_password = "pleasehackme"


def send_email_to_users(subject, body):
    user_list = Database.get_user_list()
    for user in user_list:
        Communicator.send_email(user.email, mailer_bot, mailer_bot_password, subject, body)

def send_text_to_users(body):
    user_list = Database.get_user_list()
    for user in user_list:
        Communicator.send_text(user.phone_number,"", body)

"""
Sends emails to a mailing list every month.
"""
def send_emails_at_end_of_month(recipients):
    while True:
        today = datetime.date.today()
        if end_of_month(today.month, today.day, today.year):
            for recipient in recipients:
                Communicator.send_email(recipient, mailer_bot, mailer_bot_password, "Testing", "Body")
        sleep_every_x_hours(6)


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


"""
Returns a boolean value for whether the year input is a leap year.

@:param year: Year to check.

@:returns A boolean value. True if the year is a leap year, false otherwise.
"""


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


"""
Checks whether an input date is at "an of the end month". For example, 1-31-2017 is an end of month.

@param month: Month input.

@:returns A boolean value, true if the date is an of the end month. False, otherwise.
"""


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
