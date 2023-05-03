"""
https://www.codechef.com/problems/PERFECTTRIO
"""


def perfectTrio(a, b, c):
    if a + b == c or a + c == b or c + b == a:
        return "YES"
    return "NO"


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b, c in testCase:
    print(perfectTrio(a, b, c))
