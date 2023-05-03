"""
https://www.codechef.com/problems/INTRDSGN
"""


def interiorDesign(x1, y1, x2, y2):
    sum1 = x1 + y1
    sum2 = x2 + y2
    return (sum2, sum1)[sum1 < sum2]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x1, y1, x2, y2 in testCase:
    print(interiorDesign(x1, y1, x2, y2))
