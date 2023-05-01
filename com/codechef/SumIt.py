"""
https://www.codechef.com/problems/SUMM
"""


def sumIt(a, b, c):
    return ("NO", "YES")[a + b == c]


T = int(input())
testcase = [map(int, input().split(" ")) for _ in range(T)]
for a, b, c in testcase:
    print(sumIt(a, b, c))
