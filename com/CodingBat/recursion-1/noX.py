"""
https://codingbat.com/prob/p118230
"""


def noX(s):
    if not s:
        return s
    s = (s[0], '')[s[0] == 'x'] + s[1:]

    return (s[0], '')[s[0] == 'x']+noX(s[1:])

print(noX("xxxnxdds"))
