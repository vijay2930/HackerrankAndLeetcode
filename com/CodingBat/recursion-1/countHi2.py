"""
https://codingbat.com/prob/p143900
"""


def countHi2(s):
    if not s:
        return 0
    count = (0, 1)[s[:2] == "hi"]
    step = (1, 2)[s[0] == "x"]
    return count + countHi2(s[step:])


