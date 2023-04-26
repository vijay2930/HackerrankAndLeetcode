"""
https://codingbat.com/prob/p184029
"""


def countHi(s):
    if not s:
        return 0
    count = (0, 1)[s[:2] == 'hi']
    return count + countHi(s[1:])
