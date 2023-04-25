"""
https://codingbat.com/prob/p153599
"""


def front_back(str):
    if len(str) >= 2:
        str = str[-1] + str[1:-1] + str[0]
    return str