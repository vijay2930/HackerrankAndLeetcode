"""
https://www.codingninjas.com/codestudio/problem-of-the-day/hard
"""
from os import *
from sys import *
from collections import *
from math import *


def max_profit(prices, k):
    n = len(prices)
    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

    def recurse(i, k, buy):
        if k == 0 or i == n:
            return 0
        if buy:
            return max(recurse(i + 1, k, False) - prices[i], recurse(i + 1, k, True))
        else:
            return max(recurse(i + 1, k - 1, True) + prices[i], recurse(i + 1, k, False))

    return recurse(0, k, True)


n = 5
k = 1
prices = [3, 4, 8, 4, 3]

print(max_profit(prices, k))
