"""
https://www.codechef.com/problems/COUGAME
"""


def coupleGame(G, B):
    return B - G


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for G, B in testCase:
    print(coupleGame(G, B))
