"""
https://codingbat.com/prob/p173401
"""


def sleep_in(weekday, vacation):
    return (weekday and vacation) or vacation or not weekday
