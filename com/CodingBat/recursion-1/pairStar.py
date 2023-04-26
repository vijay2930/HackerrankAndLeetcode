"""
https://codingbat.com/prob/p158175
"""


def pairStar(s):
    if len(s) == 1:
        return s
    s = (s[0], s[0] + "*")[s[0] == s[1]] + s[1:]
    return s[0] + pairStar(s[1:])


