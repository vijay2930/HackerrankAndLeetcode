"""
https://codingbat.com/prob/p189616
"""


def count_evens(nums):
    count = 0
    for val in nums:
        if val % 2 == 0:
            count += 1
    return count
