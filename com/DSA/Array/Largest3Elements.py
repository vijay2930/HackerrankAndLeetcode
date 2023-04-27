"""
https://www.geeksforgeeks.org/find-the-largest-three-elements-in-an-array/
"""


def get_largest_elements(nums):
    first = float("-inf")
    second = float('-inf')
    third = float('-inf')
    for val in nums:
        if first < val:
            third = second
            second = first
            first = val
        elif second < val and first != val:
            third = second
            second = val
        elif third < val and second != val:
            third = val
    print(first, second, third)


get_largest_elements([10, 4, 3, 50, 23, 90])
