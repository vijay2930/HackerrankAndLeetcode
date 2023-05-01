"""
https://www.codechef.com/problems/CANDIVIDE
"""


def candyDivision(candy):
    return ("NO", "YES")[candy % 3 == 0]


T = int(input())
total_candy = [int(input()) for _ in range(T)]
for candy in total_candy:
    print(candyDivision(candy))
