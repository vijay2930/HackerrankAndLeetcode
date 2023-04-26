"""
https://codingbat.com/prob/p161124
"""


def countAbc(s):
    if len(s) < 3:
        return 0
    count = (0, 1)[s[:3] == 'abc']
    return count + countAbc(s[1:])

