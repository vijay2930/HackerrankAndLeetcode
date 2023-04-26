"""
https://codingbat.com/prob/p170924
"""


def changePi(s):
    if not s:
        return s
    s = (s[:2], '3.14')[s[:2] == 'pi']+s[2:]
    return s[0] + changePi(s[1:])
