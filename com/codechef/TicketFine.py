"""
https://www.codechef.com/problems/TCKTFINE
"""


def ticketFine(x, p, q):
    return x * (p - q)


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, p, q in testCase:
    print(ticketFine(x, p, q))
