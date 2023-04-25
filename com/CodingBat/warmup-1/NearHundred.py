"""
https://codingbat.com/prob/p124676
"""


def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
