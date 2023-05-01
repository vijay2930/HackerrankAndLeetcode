"""
https://www.codechef.com/problems/BULLBEAR
"""


def bullOrBear(brought, sold):
    if brought > sold:
        return "LOSS"
    elif brought < sold:
        return "PROFIT"
    else:
        return "NEUTRAL"


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for brought, sold in testCase:
    print(bullOrBear(brought, sold))
