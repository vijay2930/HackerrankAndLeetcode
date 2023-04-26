"""
https://codingbat.com/prob/p108886
"""


def sum67(nums):
    sum = 0
    skip = False
    for val in nums:
        if val == 6:
            skip = True
        if not skip:
            sum += val
        if val == 7:
            skip = False
    return sum
