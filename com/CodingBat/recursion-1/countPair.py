"""
https://codingbat.com/prob/p154048
"""


def countPairs(str):
    if len(str) < 3:
        return 0

    if str[0] == str[2]:
        return 1 + countPairs(str[1:])
    else:
        return countPairs(str[1:])

