"""
https://www.codechef.com/problems/PASSTHEEXAM
"""


def passTheExam(a, b, c):
    return ("FAIL", "PASS")[a >= 10 and b >= 10 and c >= 10 and a + b + c >= 100]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b, c in testCase:
    print(passTheExam(a, b, c))
