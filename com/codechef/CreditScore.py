"""
https://www.codechef.com/problems/CREDSCORE
"""


def creditScore(x):
    return ("NO", "YES")[x >= 750]


x = int(input())
print(creditScore(x))
