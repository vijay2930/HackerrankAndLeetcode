"""
https://www.codechef.com/problems/M1ENROL
"""


def math1Enrolment(x, y):
    return (0, y - x)[y - x < 0]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(math1Enrolment(x, y))
