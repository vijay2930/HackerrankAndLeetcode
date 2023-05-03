"""
https://www.codechef.com/problems/HEIGHTRATION
"""


def heightOfRationals(a, b):
    return (a, b)[a < b]


a, b = map(int, input().split(" "))
print(heightOfRationals(a, b))
