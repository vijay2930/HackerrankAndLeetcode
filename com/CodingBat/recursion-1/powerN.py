"""
https://codingbat.com/prob/p158888
"""


def powerN(base, n):
    if n == 1:
        return base
    return base * powerN(base, n - 1)

print(powerN(3,3))
