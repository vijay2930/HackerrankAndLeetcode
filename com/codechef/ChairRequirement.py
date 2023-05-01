"""
https://www.codechef.com/problems/CHAIRS_
"""



def chairRequirement(x, y):
    return (0,x-y)[x>y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for x, y in testCase:
    print(chairRequirement(x, y))


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for x, y in testCase:
    print(chairRequirement(x, y))
