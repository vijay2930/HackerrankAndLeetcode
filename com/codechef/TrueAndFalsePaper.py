"""
https://www.codechef.com/problems/TFPAPER
"""


def trueAndFalsePaper(n, k):
    return n - k


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for n, k in testCase:
    print(trueAndFalsePaper(n, k))
