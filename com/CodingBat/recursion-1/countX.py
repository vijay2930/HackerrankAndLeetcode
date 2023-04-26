"""
https://codingbat.com/prob/p170371
"""


def countX(s):
    if not s:
        return 0
    count = (0, 1)[s[0] == 'x']
    return count + countX(s[1:])

print(countX("xxhixx"))