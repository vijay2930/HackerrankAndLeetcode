"""
https://codingbat.com/prob/p118182
"""


def strCount(s, sub, n):
    if not s:
        return n == 0
    count = (0, 1)[s[:len(sub)] == sub]
    return strCount(s[1:], sub, n - count)


