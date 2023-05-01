from os import *
from sys import *
from collections import *
from math import *

"""
https://www.codingninjas.com/codestudio/problem-of-the-day/easy
"""
def findLeaders(elements, n):
    # Write your code here.
    res = []
    res.append(elements[-1])
    for i in range(n - 2, -1, -1):
        if res[0] < elements[i]:
            res.insert(0, elements[i])
    return res



# Taking input using fast I/O.
def takeInput():
    n = int(input())
    elements = list(map(int, input().strip().split(" ")))

    return n, elements


# Main.
t = int(input())
while t:
    n, elements = takeInput()
    answer = findLeaders(elements, n)
    for ans in answer:
        print(ans, end=" ")
    print()
    t = t - 1
