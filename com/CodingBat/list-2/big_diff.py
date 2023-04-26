"""
https://codingbat.com/prob/p184853
"""

def big_diff(nums):
    max=float("-inf")
    min=float('inf')
    for val in nums:
        if val>max:
            max=val
        if val<min:
            min=val
    return max-min