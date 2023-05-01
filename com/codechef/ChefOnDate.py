"""
https://www.codechef.com/problems/CHEFONDATE
"""


def ChefOnDate(dollar, bill):
    return ("NO", "YES")[dollar >= bill]


T = int(input())
total_dollars = [map(int, input().split(" ")) for _ in range(T)]
for dollar, bill in total_dollars:
    print(ChefOnDate(dollar, bill))
