"""
https://www.codechef.com/problems/CREDS
"""


def numberOfCredits(x, y, z):
    return 4 * x + y * 2 + z * 0


T = int(input())
testcase = [map(int, input().split(" ")) for _ in range(T)]
for x, y, z in testcase:
    print(numberOfCredits(x, y, z))
