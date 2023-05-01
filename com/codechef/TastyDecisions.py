"""
https://www.codechef.com/problems/TASTEDEC
"""

T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]


def tastyDecision(chocolate, candy):
    candyTaste = candy * 5
    chocolateTaste = chocolate * 2
    if chocolateTaste == candyTaste:
        return "Either"
    elif chocolateTaste > candyTaste:
        return "Chocolate"
    else:
        return "Candy"


for chocolate, candy in testCase:
    print(tastyDecision(chocolate, candy))
