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

