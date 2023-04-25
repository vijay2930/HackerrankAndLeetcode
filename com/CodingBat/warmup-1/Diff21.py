"""
https://codingbat.com/prob/p197466
"""


def diff21(n):
    diff = 21 - n
    return diff if diff >= 0 else diff * -1 * 2
