"""
https://www.codechef.com/problems/FOOTCUP
"""


def footballCup(x, y):
    if x == 0 and y == 0:
        return "NO"
    return ("NO", "YES")[x == y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(footballCup(x, y))
