"""
https://www.codechef.com/problems/DETSCORE
"""

T = int(input())
total_test_cases=[list(map(int,input().split())) for _ in range(T)]
for points,test_cases in total_test_cases:
    print(points//10*test_cases)
