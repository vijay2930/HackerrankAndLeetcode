"""
https://codingbat.com/prob/p167025
"""


def sum13(nums):
    sum = 0
    skip=False
    for val in nums:
        if val == 13:
            skip=True
            continue
        if not skip:
            sum += val
        skip=False
    return sum


    return sum
print(sum13([1, 2, 2, 1,13]))
