"""
https://www.codechef.com/problems/REACH_HOME
"""


def reachHome(x, y):
    return ("NO", "YES")[x * 5 >= y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(reachHome(x, y))
