
import time


def sleepEveryXSeconds(interval):
    time.sleep(interval)


def sleepEveryXMinutes(interval):
    sleepEveryXSeconds(interval * 60)


def sleepEveryXHours(interval):
    sleepEveryXMinutes(interval * 60)


def sleepEveryXDays(interval):
    sleepEveryXHours(interval * 24)


def sleepEveryXWeeks(interval):
    sleepEveryXDays(interval * 7)


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
