"""
https://codingbat.com/prob/p126968
"""


def centered_average(nums):
    nums.remove(min(nums))
    nums.remove(max(nums))

    average = sum(nums) // len(nums)

    return average

