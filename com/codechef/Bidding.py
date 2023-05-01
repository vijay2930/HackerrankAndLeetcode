"""
https://www.codechef.com/problems/AUCTION
"""


def bidding(a, b, c):
    maxBidding = (a, b)[a < b]
    if maxBidding < c:
        return "Charlie"
    elif maxBidding == b:
        return "Bob"
    else:
        return "Alice"


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b, c in testCase:
    print(bidding(a, b, c))
