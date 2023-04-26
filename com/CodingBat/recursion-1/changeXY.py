"""
https://codingbat.com/prob/p101372
"""


def changeXY(s):
    if not s:
        return s
    s = (s[0], 'y')[s[0] == 'x'] + s[1:]
    return s[0] + changeXY(s[1:])
