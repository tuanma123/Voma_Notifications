import time


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


def days_in_the_month(month, is_leap_year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if is_leap_year:
            return 29
        else:
            return 28
    else:
        return 30


def days_left_in_month(month, day, is_leap_year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31 - day
    elif month == 2:
        return 29 - day if is_leap_year else 28 - day
    else:
        return 30 - day