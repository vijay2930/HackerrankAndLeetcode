"""
https://www.codechef.com/problems/INCRIQ
"""


def increaseIQ(x):
    return ("NO", "YES")[x + 7 > 170]


x = int(input())
print(increaseIQ(x))
