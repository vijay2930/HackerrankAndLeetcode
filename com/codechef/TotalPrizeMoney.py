"""
https://www.codechef.com/problems/PRIZEPOOL
"""

T=int(input())
testCase=[map(int,input().split(" ")) for _ in range(T)]
def totalPrizeMoney(x,y):
    return x*10+y*90

for x,y in testCase:
    print(totalPrizeMoney(x,y))