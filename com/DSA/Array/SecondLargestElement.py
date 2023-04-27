"""
https://www.geeksforgeeks.org/find-second-largest-element-array/
"""


def second_largest_element(nums):
    first=second=float('-inf')
    for val in nums:
        if first<val:
            second=first
            first=val
        elif second<val and first!=val:
            second=val
    return second

print(second_largest_element([1,2,3,4,5,6]))
