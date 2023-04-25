"""
https://codingbat.com/prob/p189441
"""


def not_string(str):
    return str if str.startswith("not") else 'not ' + str
