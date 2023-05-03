"""
https://www.codechef.com/problems/BROKENPHONE
"""


def brokenPhone(x, y):
    if x == y:
        return "ANY"
    return ("NEW PHONE", "REPAIR")[x < y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(brokenPhone(x, y))
