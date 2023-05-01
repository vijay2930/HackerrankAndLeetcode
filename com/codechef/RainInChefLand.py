"""
https://www.codechef.com/problems/RAINFALL1
"""


def rainInChefLand(x):
    if x < 3:
        return "LIGHT"
    elif 3 <= x < 7:
        return "MODERATE"
    else:
        return "HEAVY"


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(rainInChefLand(x))
