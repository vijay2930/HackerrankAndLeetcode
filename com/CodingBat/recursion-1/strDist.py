"""
https://codingbat.com/prob/p195413
"""


def strDist(str, sub):
    if len(str) < len(sub):
        return 0

    if str[:len(sub)] == sub and str[-len(sub):] == sub:
        return len(str)
    elif str[:len(sub)] == sub:
        return strDist(str[:-1], sub)
    elif str[-len(sub):] == sub:
        return strDist(str[1:], sub)
    else:
        return strDist(str[1:-1], sub)

