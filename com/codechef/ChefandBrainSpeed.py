"""
https://www.codechef.com/problems/CBSPEED
"""


def chefAndBrainSpeed(x, y):
    return ("NO", "YES")[x < y]


x, y = map(int, input().split(" "))
print(chefAndBrainSpeed(x, y))
