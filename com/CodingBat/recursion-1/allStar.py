"""
https://codingbat.com/prob/p183394
"""


def allStar(s):
    if len(s) == 1:
        return s
    return s[0] + "*" + allStar(s[1:])


print(allStar("hello"))
