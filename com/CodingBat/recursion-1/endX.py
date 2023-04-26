"""
https://codingbat.com/prob/p105722
"""


def endX(s):
    if not s:
        return s
    if s[0] == "x":
        return "" + endX(s[1:]) + 'x'
    return s[0] + endX(s[1:])


