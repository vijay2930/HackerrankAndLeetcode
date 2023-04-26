"""
https://codingbat.com/prob/p167015
"""


def count11(s):
    if len(s) < 2:
        return 0
    count = (0, 1)[s[:2] == '11']
    return count + count11(s[count + 1:])
