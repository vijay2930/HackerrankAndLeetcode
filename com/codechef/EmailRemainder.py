"""
https://www.codechef.com/problems/EMAILREM
"""


def emailRemainder(n, u):
    return n - u


n, u = map(int, input().split(" "))
print(emailRemainder(n, u))
