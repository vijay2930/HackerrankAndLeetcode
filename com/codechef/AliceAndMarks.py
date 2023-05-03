"""
https://www.codechef.com/problems/MARKSTW
"""


def aliceAndMarks(x, y):
    return ("NO", "YES")[x > y]


x,y=map(int,input().split(" "))

print(aliceAndMarks(x,y))